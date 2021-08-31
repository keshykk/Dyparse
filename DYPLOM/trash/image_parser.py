import csv
import os
import requests

with open('Sushi.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter="|")
    for row in reader:
        image = row[3]
        if(image !='Link'):
            url = 'https://sushi-master.pl' + image
            filename = image.split('/')[-1]

            if not os.path.exists('uploads'):
                os.mkdir('uploads')
            img_data = requests.url.content
            with open('uploads' + '/' + filename, 'wb') as handler:
                handler.write(img_data)
            print(filename)
