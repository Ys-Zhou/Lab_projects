import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.asahi.com/'
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')

access_ranking = soup.find('dl', class_='Ranking', id='AccessTop_list')

with open('asahi_ranking.txt', 'w+', encoding='utf-8') as f:
    for link in access_ranking.find_all('a'):
        f.write(link.string)
        f.write('\n')
        f.write(link.get('href'))
        f.write('\n')
