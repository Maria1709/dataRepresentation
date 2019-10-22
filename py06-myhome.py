<import requestws
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")

soup = BeautifulSoup(page.cotent, 'html.parser')
print (soup.prettify())
