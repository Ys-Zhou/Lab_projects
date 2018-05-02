import MeCab
from DBConnector import GetCursor

tagger = MeCab.Tagger('-Ochasen')
print(tagger.parse("すもももももももものうち"))

with GetCursor() as cur:
    cur.execute('SELECT * FROM ips.detail')
    for row in cur:
        print(row)
