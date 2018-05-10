import MeCab
import threading
from DBConnector import GetCursor

# Get tagger
tagger = MeCab.Tagger()

# Unwilling words
ng_genkei = ['*']
ng_hinshi = ['BOS/EOS', '記号']

# Template of insert query
insert = 'INSERT INTO `lab`.`bow2` (`genkei`, `hinshi`) VALUES (%s, %s)'


class ParseFileThread(threading.Thread):

    def __init__(self, file_path):
        super(ParseFileThread, self).__init__()
        self.__file_path = file_path

    def run(self):
        print('Start parse file: %s' % self.__file_path)
        self.__do_parse()

    def __do_parse(self):
        # Insert values
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

        # Execute query
        with GetCursor() as cur:
            cur.executemany(insert, values)


if __name__ == '__main__':

    thread_pool = []

    for file_num in range(1, 6):
        thread = ParseFileThread('../_2_parse_page/%d.txt' % file_num)
        thread.start()
        thread_pool.append(thread)

    for thread in thread_pool:
        thread.join()
