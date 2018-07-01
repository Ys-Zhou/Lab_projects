from twconnector import TwitterConnector
from dbconnector import GetCursor


def get_tweets(user_id: str):
    # https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

    params = {
        'user_id': user_id,
        'count': 10
    }

    values = []
    for tweet in TwitterConnector().get_json_res(url, params):
        values.append((tweet['id_str'], tweet['user']['name'], tweet['text']))

    insert = 'INSERT INTO tweets (id, user, text) VALUES (%s, %s, %s)'
    with GetCursor() as cur_1:
        cur_1.executemany(insert, values)


if __name__ == '__main__':
    query = 'SELECT DISTINCT follow_id FROM followee'
    with GetCursor() as cur:
        cur.execute(query)
        for row in cur:
            get_tweets(row[0])
