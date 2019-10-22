from bs4  import BeautifulSoup
with open("../week02/carview2.html") as fp.
    soup = BeautifulSoup(fp, 'html.parser')

print (soup.tr)

rows = soup.findall("tr")
for row in rows:
    print("_________")
    print(row)
    cols = row.findAll("td")
    for col in cols:
        print(col.text)

datalist = []
    for cols in cols:
        dataList.append(col.text)
    print(dataList)
