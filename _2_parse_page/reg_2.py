import urllib.request
import re

url = 'http://www.asahi.com/'
page = urllib.request.urlopen(url).read().decode('utf-8')

with open('links.txt', 'w+', encoding='utf-8') as f:
    for match in re.finditer('<a.+?href="(.+?)"', page, re.DOTALL):
        f.write(match.group(1))
        f.write('\n')
