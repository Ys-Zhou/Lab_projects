import urllib.request
from bs4 import BeautifulSoup

with open('asahi_ranking.txt', 'r', encoding='utf-8') as f:
    line = 0
    for link in f:
        line += 1
        if line % 2 == 0:
            page = urllib.request.urlopen(link).read()
            soup = BeautifulSoup(page, 'html.parser')
            text = soup.find('div', class_='ArticleText')

            filename = '%d.txt' % (line / 2)
            with open(filename, 'w+', encoding='utf-8') as text_f:
                for paragraph in text.find_all('p'):
                    text_f.write(paragraph.string)
                    text_f.write('\n')
