import oauth2
import json
 

class TwitterConnector:

    def __init__(self):
        api_k = 'nMHgXLTw05yT1f8sQxkgXidxG'  # API Key
        api_s = 'hrxokm8ErYfA8pt2n2LaIfAHv2x1qv2sz2IxvQaoyMkF4qPzOq'  # API Secret
        at = '736421314366312448-0Hg5SeJvi9C7updp62rP9PzDRkcANjP'  # Access Token
        at_s = 'ByWdBKaJ06Qi4hCkubIhTdE5BMXKgo8jEWqh1HNMGeufM'  # Accesss Token Secert

    def oauth_req(self, url, http_method='GET', post_body='', http_headers=None):
        consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        token = oauth2.Token(key=key, secret=secret)
        client = oauth2.Client(consumer, token)
        resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
        return content

    # def getJSON(self, iUrl, iParams):
    #
    #     req = self.__twitter.get(iUrl, params=iParams)
    #     if req.status_code == 200:
    #         text = json.loads(req.text)
    #         return text
    #     else:
    #         # Report error
    #         print("Error: %d" % req.status_code)
