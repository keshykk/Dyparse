import pymysql
import pandas as pd
import csv
#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="wsd" )
cursor = connection.cursor()
data1 = pd.read_csv(r'D:\DYPLOM\Menu.csv', sep = '|', header = 0)
data1.colums = ['Nazwa', 'Skladniki', 'Cena']
df = pd.DataFrame(data = data1, columns= ['Nazwa', 'Skladniki', 'Cena'])
# some other statements  with the help of cursor
# Query for creating table
DROPTAB = """DROP TABLE IF EXISTS people"""
MaxPiz = """ CREATE TABLE people (NAZWA varchar(1000), OPIS varchar(1000), CENA numeric);"""
cursor.execute(DROPTAB)
cursor.execute(MaxPiz)
for row in df.itertuples():
    cursor.execute("""
                INSERT INTO wsd.dbo.people (NAZWA, OPIS, CENA)
                VALUES (?,?,?)""", (row.Nazwa,row.Skladniki,row.Cena))
conn.commit()

connection.close()
