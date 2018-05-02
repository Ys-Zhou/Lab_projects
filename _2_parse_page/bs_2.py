import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.asahi.com/'
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')

with open('links.txt', 'w+', encoding='utf-8') as f:
    for link in soup.find_all('a'):
        f.write(link.get('href'))
        f.write('\n')
