from TwitterConnector import TwitterConnector
from DBConnector import GetCursor

# https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

params = {
    'count': 10
}

values = []
for tweet in TwitterConnector().get_json_res(url, params):
    values.append((tweet['id_str'], tweet['user']['name'], tweet['text']))

insert = 'INSERT INTO tweets (id, user, text) VALUES (%s, %s, %s)'
with GetCursor() as cur:
    cur.executemany(insert, values)
