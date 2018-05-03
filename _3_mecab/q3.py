import MeCab
from DBConnector import GetCursor

# Get tagger
tagger = MeCab.Tagger()

# Word filters
genkei_flt = ['*']
hinshi_flt = ['BOS/EOS', '記号']

# Insert SQL template
insert = 'INSERT INTO `lab`.`bow2` (`genkei`, `hinshi`) VALUES (%s, %s)'

# Create a cursor
with GetCursor() as cur:
    # Read text: files -> file -> line
    for file_num in range(1, 2):
        file_name = '../_2_parse_page/%d.txt' % file_num
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f:
                # Parse each word
                word = tagger.parseToNode(line)
                while word:
                    feature_list = word.feature.split(',')
                    genkei, hinshi = feature_list[6], feature_list[0]
                    # If the word is supposed, execute insert
                    if genkei not in genkei_flt and hinshi not in hinshi_flt:
                        cur.execute(insert, (genkei, hinshi))
                    word = word.next
