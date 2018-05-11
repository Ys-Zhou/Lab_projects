from _4_twitter.TwitterConnector import TwitterConnector
from DBConnector import GetCursor

url = 'https://api.twitter.com/1.1/friends/ids.json'

my_id = '736421314366312448'

values = []
for friend_id in TwitterConnector().get_json_res(url)['ids']:
    values.append((my_id, friend_id))

insert = 'INSERT INTO `lab`.`followee` (`from_id`, `follow_id`) VALUES (%s, %s)'
with GetCursor() as cur:
    cur.executemany(insert, values)
