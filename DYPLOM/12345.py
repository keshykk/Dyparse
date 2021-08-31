import bs4
import io
import sqlite3
from sqlite3.dbapi2 import Cursor
from sys import argv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# database connection
# connection = pymysql.connect(host="localhost",user="root",passwd="",database="wsd")
connection = sqlite3.connect('Baza1.sql')
cursor: Cursor = connection.cursor()
MaxPiz = """CREATE TABLE MaxiPizza(
NAZWA TEXT,
OPIS  TEXT,
CENA REAL)"""

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute(MaxPiz)
    quit()

my_url = 'https://www.maxipizza.pl/kielce,menu,internet'

# Połączenie oraz pobranie strony
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parsowanie HTML
page_soup = soup(page_html, "html.parser")

# określenie frejma produktu
containers = page_soup.findAll("div", {"class": "pizza-placeholder"})
container = containers[0]
tekst = container.h4.get_text()


# Funkcja do znormalizowania HTML
def multiple_replace(target_str, replace_values):
    # pętla dla pobierania danych do zamiany
    for i, j in replace_values.items():
        # zamiana target_str
        target_str = target_str.replace(i, j)
    return target_str


# słownik wartości do zamiany
replace_values = {"\n": "", "\t": "", "\r": "", "1/2": ""}
# zmiana wartości początkowej
my_str = multiple_replace(tekst, replace_values)

for container in containers:
    nazwy = container.findAll("h4", {"class": "towar-nazwa"})
    nazwas = nazwy[0].get_text()
    nazwa = multiple_replace(nazwas, replace_values)
    opis_piz = container.findAll("span", {"class": "towar-description"})
    opis_pizz = opis_piz[0].get_text()
    ceny = container.findAll("div", {"class": "towar-cena"})
    cena_0 = ceny[0]
    cena11 = cena_0.get_text().replace("zł", "").replace(",", ".")
    cena = cena11

    print("nazwa: " + nazwa)
    print("opis: " + opis_pizz)
    print("cena: " + cena)
    cursor.execute('INSERT INTO MaxiPizza VALUES (?, ?, ?)', (nazwa, opis_pizz, cena))
    connection.commit()

# allnazwa = []
# for container in containers:
#   lista = []
#  for nazwa in containers:
#     lista.append(nazwa)
# allnazwa.append(lista)

# cursor.executemany('''INSERT INTO MaxiPizza(NAZWA) VALUES (?)''', nazwa)

connection.close()

