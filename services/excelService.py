import openpyxl

def create_excel(data, filename="reporte.xlsx"):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(filename)
