from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.maxipizza.pl/kielce,menu,internet#product-list-container'

# Połączenie oraz pobranie strony 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parsowanie HTML
page_soup = soup(page_html, "html.parser")

#określenie frejma produktu
containers = page_soup.findAll("div", {"class":"pizza-placeholder"})
container = containers[0]

for container in containers:
	nazwa = container.h4
	print("nazwa" + nazwa + "\n")

