import xlwt

#program untuk membuat data xcel menggunakan modul xlwt

kota = ['Solo', 'Bandung', 'Surabaya']
provinsi = ['Jawa Tengah', 'Jawa Barat', 'Jawa Timur']

wb = xlwt.Workbook() #membuat xls

ws = wb.add_sheet('Data Kota') #menambahkan shhet

ws.write(0, 0, 'Nama Kota')
ws.write(0, 1, 'Provinsi' )

i= 1

for a,b in zip(kota, provinsi):
    ws.write(i, 0, a)
    ws.write(i, 1, b)
    i+=1

wb.save('data-kota.xls')
print('Data tersimpan')