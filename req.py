from bs4 import BeautifulSoup as bs
from openpyxl import load_workbook
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module="openpyxl")
html = open("state_req.html", "w")

doc = open("index.html", "r")
soup = bs(doc, "html.parser")

d = soup.find_all('h2', string='A')


wb = load_workbook(filename='state_req.xlsx')
ws = wb['Checklist 4']
alphabet = "abcdefghijklmnopqrstuvwxyz"


def insert_heading(body, letter):
    #find the column Then insert the h2 and letter. Then add an line
    #return the body


for cell in ws:
    if cell[1].value:
        if cell[1].value[0].lower() in alphabet:
            print(cell[1].value[0])
            letter = soup.find('h2', string=cell[1].value[0])
            if letter:
                print("theres a letter")
            else:
                print("need to generate one")

            # li = soup.new_tag('li')
            # char = cell[1].value[0] # print(i[1].value[0])
            # elem = soup.find('ul', {'id': char})
            # print(elem)
            # tag = soup.new_tag("a")
            
            # tag.string = cell[1].value
            # tag.attrs['href'] = cell[5].value
            # li.insert(0, tag)

            # if elem:
            #     elem.insert_after(li)
        # else:
            # li = soup.new_tag('li')
            # elem = soup.find('ul', {'id': 'Other'})
            # tag = soup.new_tag("a")
            
            # tag.string = cell[1].value
            # tag.attrs['href'] = cell[5].value
            # li.insert(0, tag)

            # if elem:
            #     elem.insert_after(li)


# f = open("test.html", "w")
# f.write(str(soup))
# f.close()




