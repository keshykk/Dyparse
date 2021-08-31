import bs4
import io
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.pyszne.pl/menu/maxi-pizza-kielce'

# Połączenie oraz pobranie strony
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
