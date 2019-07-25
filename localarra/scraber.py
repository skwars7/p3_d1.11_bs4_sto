import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/'
response = requests.get(url)
html = response.content
#soup = BeautifulSoup(html)
soup = BeautifulSoup(html, "html.parser")
table = soup.find('div', attrs={'class': 'narrow'})
print(table)
list_of_rows = []
for row in table.findAll('div', attrs={'class':'summary'}):
    list_of_cells = []
    for cell in row.findAll('h3'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
print(list_of_rows)