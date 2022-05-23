import openpyxl
import json
import pyexcel as p

#excel_file = 'C:\Users\82105\Desktop\신희승\IIRTECH\IIRTECH\data.xlsx'
json_file = 'C:\\Users\\82105\\Desktop\\신희승\\IIRTECH\\IIRTECH\\data.json'
excel_file = 'C:\\Users\\82105\\Desktop\\신희승\\IIRTECH\\IIRTECH\\data.xlsx'

# xls to xlsx
#p.save_book_as(file_name = excel_file, dest_file_name= excel_file+"x")

wb = openpyxl.load_workbook(excel_file, read_only=True)

sheet = wb.worksheets[1]

# key_list 생성
col_max = sheet.max_column
row_max = sheet.max_row
key_list = []
for i in range(1,col_max+1):
    key_list.append(sheet.cell(row=1, column=i).value)
data_dict = {}
key_index = 0
for row_num in range(2, row_max):
    tmp_dict = {}
    if row_num % 10 == 0:
        print(row_num)
    for i in range(1, col_max+1):
        val = sheet.cell(row=row_num, column=i).value
        tmp_dict[key_list[i-1]] = val
    data_dict[tmp_dict[key_list[0]] + tmp_dict[key_list[1]]] = tmp_dict
wb.close()

with open(json_file, 'w', encoding='utf-8') as fp:
    json.dump(data_dict, fp, indent=4, ensure_ascii=False)
