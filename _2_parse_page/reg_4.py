import urllib.request
import re

with open('asahi_ranking.txt', 'r', encoding='utf-8') as f:
    line = 0
    for link in f:
        line += 1
        if line % 2 == 0:
            page = urllib.request.urlopen(link).read().decode('utf-8')
            text = re.search('<div class="ArticleText">(.+?)</div>', page, re.DOTALL)

            filename = '%d.txt' % (line / 2)
            with open(filename, 'w+', encoding='utf-8') as text_f:
                for paragraph in re.finditer('<p>(.+?)</p>', text.group(1), re.DOTALL):
                    text_f.write(paragraph.group(1))
                    text_f.write('\n')
