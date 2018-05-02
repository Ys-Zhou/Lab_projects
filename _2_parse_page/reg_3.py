import urllib.request
import re

url = 'http://www.asahi.com/'
page = urllib.request.urlopen(url).read().decode('utf-8')

access_ranking = re.search('<dl class="Ranking" id="AccessTop_list">(.+?)</dl>', page, re.DOTALL)

with open('asahi_ranking.txt', 'w+', encoding='utf-8') as f:
    for link in re.finditer('<a href="(.+?)">(.+?)</a>', access_ranking.group(1)):
        f.write(link.group(2))
        f.write('\n')
        f.write(link.group(1))
        f.write('\n')
