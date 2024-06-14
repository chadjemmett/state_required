from bs4 import BeautifulSoup as bs
from openpyxl import load_workbook
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module="openpyxl")
html = open("state_req.html", "w")

links = []

doc = open("index.html", "r")
soup = bs(doc, "html.parser")

wb = load_workbook(filename='test_sheet.xlsx')
ws = wb['sheet']

for i in ws:
    if i[0].offset(1, 1).value and i[0].value:
        cur_cell = i[0].offset(1, 1)
        print(i[0].value)
        while cur_cell.offset(1, 0).value:
            print("\t",cur_cell.value)
            cur_cell = cur_cell.offset(1, 0)
        print("\t", cur_cell.value)
    elif i[0].value:
        print(i[0].value)

            
        # cur_cell = i[0].offset(1, 1)
        # while cur_cell.offset(1, 0).value:
        #     cur_cell = cur_cell.offset(1, 0)
        #     print(i[0].value, "\n\t", cur_cell.value)

# cur_cell = ws.cell(31, 1)
# while cur_cell.offset(1, 0).value:
#     print(cur_cell.value)
#     cur_cell = cur_cell.offset(1, 0)

# print(cur_cell.value)

html.close()
