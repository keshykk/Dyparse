from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://biesiadowo.pl/z-kielce-ul-kozia'

#Połączenie ze stroną
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("p", {"class":"bold menu-item-name"})
opis = page_soup.findAll("p", {"class":"small food-description read-more"})
cena = page_soup.findAll("span", {"class":"bold priceItemList"})
ceny = cena[0]
opisy = opis[0]  
container = containers[0]

for container in containers:
	nazwa = container.text 
