import MeCab
from DBConnector import GetCursor
from collections import Counter

tagger = MeCab.Tagger()


def cal_tf(uid: str, text: str):
    word = tagger.parseToNode(text)

    # Parse words
    nouns = []
    while word:
        feature_list = word.feature.split(',')
        prototype, vocabulary = feature_list[6], feature_list[0]
        if vocabulary == '名詞' and prototype != '*':
            nouns.append(prototype)
        word = word.next

    # Calculate tf
    num = len(nouns)
    cnt = Counter(nouns)

    insert = 'INSERT INTO tf (uid, word, tf) VALUES (%s, %s, %s)'

    values = []
    for key, val in cnt.items():
        tf = val / num
        values.append((uid, key, tf))

    with GetCursor() as sub_cur:
        sub_cur.executemany(insert, values)


if __name__ == '__main__':
    with GetCursor() as cur:
        query = 'SELECT uid, tweets FROM docs'
        cur.execute(query)
        for row in cur:
            cal_tf(row[0], row[1])
