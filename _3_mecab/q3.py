import MeCab
import threading
from DBConnector import GetCursor

# Get tagger
tagger = MeCab.Tagger()

# Word filters
ng_genkei = ['*']
ng_hinshi = ['BOS/EOS', '記号']

# Template of insert query
insert = 'INSERT INTO `lab`.`bow2` (`genkei`, `hinshi`) VALUES (%s, %s)'


class ParseFileThread(threading.Thread):

    def __init__(self, file_path):
        super(ParseFileThread, self).__init__()
        self.__file_path = file_path

    def run(self):
        self.__do_parse()

    def __do_parse(self):
        values = []

        with open(self.__file_path, 'r', encoding='utf-8') as fl:
            for line in fl:
                # Parse each word
                word = tagger.parseToNode(line)
                while word:
                    feature_list = word.feature.split(',')
                    genkei, hinshi = feature_list[6], feature_list[0]
                    # Filter out supposed word
                    if genkei not in ng_genkei and hinshi not in ng_hinshi:
                        values.append((genkei, hinshi))
                    word = word.next

        with GetCursor() as cur:
            cur.executemany(insert, values)


for file_num in range(1, 2):
    file_path_ = '../_2_parse_page/%d.txt' % file_num
