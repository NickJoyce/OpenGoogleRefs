#! python3
# Выполняет поиск в google по запросу (query), открывает в браузере первые num_open страниц
# выданных google в результатах поиска

import webbrowser
import requests
from bs4 import BeautifulSoup

query = 'Театры москвы'
num_open = 5

headers = {
    "Accept":"*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}

res = requests.get(f'https://www.google.com/search?q={query}&sourceid=chrome&ie=UTF-8', headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

link_elems = soup.find_all('div', class_="yuRUbf")

num_open = min(num_open, len(link_elems))

for i in range(num_open):
    webbrowser.open(link_elems[i].find('a').get('href'))