import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")

soup = BeautifulSoup(page.cotent, 'html.parser')
print (soup.prettify())

##listings = soup.find("div", class_="PropertyListingCard")
##print (listings)

##price = listings.find(class_="PropertyLisingCard_Price")
##print price

listings = soup.findALl("div", class_="PropertyListingCard" )

for listing in listings:
    entry = []

    price = listing.find(class_="PropertyListingCard_Price").text
    entry.append(price)
    address - listing.find(class_-"PropertyListingCard_Address").text
    entryList.append(address)
    
    home_writer.writerow(entryList)
home_file.close()