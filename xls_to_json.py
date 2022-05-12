import openpyxl
import json
import pyexcel as p

excel_file = 'D:\신희승\IIRTECH\data2\963510_50000.xls'
json_file = 'D:\신희승\IIRTECH\data2\963510_50000.json'

p.save_book_as(file_name = excel_file, dest_file_name= excel_file+"x")
# 엑셀 열기

excel_file = 'D:\신희승\IIRTECH\data\963510_50000.xlsx'
wb = openpyxl.load_workbook(excel_file, read_only=True)

sheet = wb.worksheets[0]

key_list = []
for col_num in range(1, 7):
    key_list.append(sheet.cell(row=1, column=col_num).value)
data_dict = {}
key_index = 0
for row_num in range(2, 100):
    tmp_dict = {}
    if row_num % 10 == 0:
        print(row_num)
    for col_num in range(1, 7):
        val = sheet.cell(row = row_num, column= col_num).value
        tmp_dict[key_list[col_num-1]] = val
    data_dict[tmp_dict[key_list[key_index]]] = tmp_dict
wb.close()

with open(json_file, 'w', encoding='utf-8') as fp:
    json.dump(data_dict, fp, indent=4, ensure_ascii=False)