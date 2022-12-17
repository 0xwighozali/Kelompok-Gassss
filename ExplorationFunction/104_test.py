def update_data_sheet(data_sheet, row, col, value): 
    '''fungsi untuk mwngupdate data xcel yang sudah ada'''
    try: 
        import xlrd
        from xlutils.copy import copy

        rb = xlrd.open_workbook(data_sheet)
        wb = copy(rb)

        sheet = wb.get_sheet('Data Kota') 
        sheet.write(row, col, value) 
        wb.save(data_sheet) 
        print('data tersimpan')
    except Exception as e: 
        print(e)

update_data_sheet('data-kota.xls', 1, 1, "Serem") #file name , columb, row, data yang mau diupdate
