from ast import Break
from docx import Document
import re

def isDate (text):
    dateRegex = re.compile(r'\s\d\d\.\d\d\.\d\d\d\d')
    mo = dateRegex.search(text)
    print('Объект Match', mo)

    if mo:
        print('Date is', mo.group())
        return mo.group().strip()
    print("Date isn't found")
    return None
    

# открываем существующий документ 
doc = Document('/home/denis/Документы/python_project/bearing_search/akt.docx')

act = None # акт
act_date = None # дата
executor = None # исполнитель
brand_size = None # бренд типоразмер 
customer = None # заказчик
recipient = None # получатель
bearing_number = None # номер подшипника
date_manufacture = None # дата изготовления
reason_transfer = None # причина передачи

# весь текст документа по абзацам
for paragraph in doc.paragraphs:
     act_date = isDate(paragraph.text)
     print(act_date)
     if act_date:        
        break

# table = doc.tables[1]

# # читаем данные из таблиц
# for table in doc.tables:
#     print(table)
#     for row in table.rows:
#         string = ''
#         for cell in row.cells:
#             string = string + cell.text + ' '
#         print(string)