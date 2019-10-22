import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("______________________")
print (page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print ("____________________")
print (soup1.prettify())
with open("C:\Users\maria\OneDrive\Desktop\dataRepresentation\car viewer.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print (soup.prettify())
