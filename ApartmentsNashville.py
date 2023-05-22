import requests
from bs4 import BeautifulSoup
import pandas as pd



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
url = "https://www.apartments.com/nashville-tn/under-1000/"
url_Res = requests.get(url, headers=headers)

Soup = BeautifulSoup(url_Res.content, 'html5lib')
data = Soup.find_all('li', class_='mortar-wrapper')

propertyTitle = []
propertyName = []
propertyAddress = []
apartmentPrice = []
bedRooms = []
propertyNumber = []

def func():

  for info in data:
    name = info.header.a.text
    propertyName.append(name)

    i = info.header.find('span', class_='js-placardTitle title').get_text()
    propertyTitle.append(i)


    x = info.header.find('div', class_="property-address js-url").get_text()
    propertyAddress.append(x)

    o = info.find('p', class_="property-pricing").get_text()
    apartmentPrice.append(o)

    br = info.find('p', class_="property-beds").get_text()
    bedRooms.append(br)

    p = info.find('a', class_="phone-link js-phone").get_text()
    propertyNumber.append(p)
func()


# Create a dataframe for the data your scrapped.
apartmentTable = pd.DataFrame({'Property Titile': propertyTitle, 'Property Name': propertyName, 'Property Address': propertyAddress, 'Apartment Price': apartmentPrice, 'Bedrooms': bedRooms, 'Phone Number': propertyNumber})
print(apartmentTable.to_string())




