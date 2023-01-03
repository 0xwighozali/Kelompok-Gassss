from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import xlwt
from .models import Bendungan



# Create your views here.
class myBendugan(object):
    def __init__(self, tinggi, lebar, panjang):
        self.tinggi = tinggi
        self.lebar = lebar
        self.panjang = panjang 
    def luas(self):
        return self.tinggi * self.lebar
    def volume(self):
        return self.panjang *self.lebar *self.tinggi


def index(request):
    context = {
        'bendungan_list' : Bendungan.objects.all()
    }
    return render(request, "bendungans/index.html", context)

def add(request):
    return render(request,'bendungans/form.html')

def save(request):
    panjang = int(request.POST['panjang'])
    lebar = int(request.POST['lebar'])
    tinggi = int(request.POST['tinggi'])
    hasil = myBendugan(tinggi, lebar, panjang)
    data = Bendungan(
        nm_bendungan = request.POST['nama'],
        lk_bendungan = request.POST['lokasi'],
        luas_bendungan = hasil.luas(),
        vlm_bendungan = hasil.volume(),
    )
    data.save()
    return HttpResponseRedirect(reverse('bendungans.index'))

def delete(request, bendungan_id):
    bd = get_object_or_404(Bendungan, pk=bendungan_id)
    bd.delete()
    return HttpResponseRedirect(reverse('bendungans.index'))

def edit(request, bendungan_id):
    bd = get_object_or_404(Bendungan, pk=bendungan_id)
    context = {
        'id' : bendungan_id,
        'nama' : bd.nm_bendungan,
        'lokasi' : bd.lk_bendungan,
    }
    return render(request, 'bendungans/edit_form.html', context)

def update(request, bendungan_id):
    bd = get_object_or_404(Bendungan, pk=bendungan_id)
    panjang = int(request.POST['panjang'])
    lebar = int(request.POST['lebar'])
    tinggi = int(request.POST['tinggi'])
    hasil = myBendugan(tinggi, lebar, panjang)
    
    bd.nm_bendungan = request.POST['nama']
    bd.lk_bendungan = request.POST['lokasi']
    bd.luas_bendungan = hasil.luas()
    bd.vlm_bendungan = hasil.volume()
    bd.save()
    return HttpResponseRedirect(reverse('bendungans.index'))

def export_data(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="bendungan.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Bendungan')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nama Bendungan', 'Lokasi Bendungan', 'Luas Bendungan', 'Volume Bendungan']

    for col_num in range(len(columns)):
        #row , col, data
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Bendungan.objects.all().values_list('nm_bendungan', 'lk_bendungan', 'luas_bendungan', 'vlm_bendungan')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response