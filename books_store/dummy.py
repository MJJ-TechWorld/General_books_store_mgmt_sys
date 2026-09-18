from datetime import datetime
from openpyxl import load_workbook
STORE_DATA_PATH = "STORE_RECORDS.xlsx"

profit1,profit2,profit3 = [],[],[]
loss1,loss2,loss3 = [],[],[]

date = datetime.today().strftime('%d-%m-%Y')

wb = load_workbook(STORE_DATA_PATH)
s = wb["Store Data"]
for row in s.iter_rows(min_row=2,values_only=False):
    if str(row[6].value).strip() == str(date):
        loss1.append(int(row[5].value))
    if str(row[6].value).strip()[:5] == str(date)[:5]:
        loss2.append(int(row[5].value))
    if str(row[6].value).strip()[-2:] == str(date)[-2:]:
        loss3.append(int(row[5].value))

wd = load_workbook(STORE_DATA_PATH)
s = wd["Users Data"]
for row in s.iter_rows(min_row=2,values_only=False):
    for row in s.iter_rows(min_row=2,values_only=False):
        if str(row[7].value).strip() == str(date):
            profit1.append(int(row[6].value))
        if str(row[7].value).strip()[:5] == str(date)[:5]:
            profit2.append(int(row[6].value))
        if str(row[7].value).strip()[-2:] == str(date)[-2:]:
            profit3.append(int(row[6].value))

p1,p2,p3 = sum(profit1),sum(profit3),sum(profit3),
l1,l2,l3 = sum(loss1),sum(loss2),sum(loss3)

print(profit1,profit1,profit3)
print(loss1,loss2,loss3)

print(p1,p2,p3)
print(l1,l2,l3)