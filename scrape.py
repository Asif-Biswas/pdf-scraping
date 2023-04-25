"""
data format
data = [
    {
        "name": "name",
        "tables": [
            "table1",
            "table2",
            "table3"
        ]  
    }
]
"""

from bs4 import BeautifulSoup
import json

html_file_path = 'pdf-scraping/index.html'
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

    # Find all the divs with the class 'calibre3'
    divs = soup.find_all('div', class_='calibre3')[9:54]

    data = []
    
    # Loop through each div
    for div in divs:
        data_format = {
            "name": "",
            "tables": []
        }
        h1 = div.find('h1', class_='h1-blue')
        name = h1.text.split('. ')[1].strip()
        data_format['name'] = name
        tables = div.find_all('table')
        for table in tables:
            # get as html string
            table = str(table)
            data_format['tables'].append(table)
        data.append(data_format)

    
# create a new json file
with open('pdf-scraping/data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
