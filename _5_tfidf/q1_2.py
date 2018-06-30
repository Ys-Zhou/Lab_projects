from TwitterConnector import TwitterConnector
from DBConnector import GetCursor


def get_tweets(screen_name: str, count: int = 100):
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {'screen_name': screen_name, 'count': count}

    tweets = TwitterConnector().get_json_res(url, params)

    uid = tweets[0]['user']['id_str']

    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet['text'])

    insert = 'INSERT INTO docs (uid, tweets) VALUES (%s, %s)'
    with GetCursor() as cur:
        cur.execute(insert, (uid, ' '.join(tweet_list)))


if __name__ == '__main__':
    user_list = ['ariyoshihiroiki', 'matsu_bouzu', 'pamyurin', 'RolaWorLD', 'hajimesyacho', 'Suzu_Mg', 'hentaimimura',
                 'takapon_jp', 'kojiharunyan', 'fashionpressnet']

    for user in user_list:
        get_tweets(user)
