from TwitterConnector import TwitterConnector
from DBConnector import GetCursor

# https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids
url = 'https://api.twitter.com/1.1/friends/ids.json'

my_id = '736421314366312448'

values = []
for friend_id in TwitterConnector().get_json_res(url)['ids']:
    values.append((my_id, friend_id))

insert = 'INSERT INTO lab.followee (from_id, follow_id) VALUES (%s, %s)'
with GetCursor() as cur:
    cur.executemany(insert, values)
