class data_excel(object):
   def __init__(self, file, sheet, col , row, value):
      self.file = file
      self.sheet = sheet
      self.col = col
      self.row = row
      self.value = value
   def update(self):
      import xlrd
      from xlutils.copy import copy
      
      rb = xlrd.open_workbook(self.file)
      wb = copy(rb)

      sheet = wb.get_sheet(self.sheet) 
      sheet.write(self.row, self.col, self.value) 
      wb.save(self.file) 
      print('data tersimpan')

data_excel1 = data_excel('data-kota.xls','Data Kota', 1, 1, "Kalimantan")
data_excel1.update()