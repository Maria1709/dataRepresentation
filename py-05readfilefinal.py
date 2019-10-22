from bs4  import BeautifulSoup
import csv

with open("../week02/carview2.html") as fp.
    soup = BeautifulSoup(fp, 'html.parser')

print (soup.tr)

employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimeter=',', quotechar='''', quoting=csv.QUOTE_MINIMAL)


rows = soup.findall("tr")
for row in rows:


    cols = row.findAll("td")
    datalist = []
    for cols in cols:
        dataList.append(col.text)
    employee_writer.writerow(datalist)
employee_file.close()
    