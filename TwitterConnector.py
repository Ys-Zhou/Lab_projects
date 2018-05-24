import oauth2
import os
import json
import xml.etree.cElementTree as cElementTree


# Singleton pattern decorator
def singleton(cls, *args, **kw):
    instance = {}

    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]

    return _singleton


@singleton
class TwitterConnector:

    def __init__(self):
        xml_tree = cElementTree.parse(os.path.join(os.path.dirname(__file__), 'config.xml'))

        consumer_node = xml_tree.find('consumer')
        csm_k = consumer_node.find('key').text
        csm_s = consumer_node.find('secret').text
        consumer = oauth2.Consumer(key=csm_k, secret=csm_s)

        token_node = xml_tree.find('token')
        tkn_k = token_node.find('key').text
        tkn_s = token_node.find('secret').text
        token = oauth2.Token(key=tkn_k, secret=tkn_s)

        self.client = oauth2.Client(consumer, token)

    def get_json_res(self, url: str, params: dict = None):
        res, text = self.__oauth_req(url, params)
        if res['status'] == '200':
            return json.loads(text)
        else:
            raise RuntimeError('Http code: %s' % res['status'])

    def __oauth_req(self, url: str, params: dict = None):
        if params is not None:
            is_first = True
            for param in params.items():
                if is_first:
                    url += '?%s=%s' % param
                    is_first = False
                else:
                    url += '&%s=%s' % param

        res, content = self.client. \
            request(url, method='GET', body=''.encode('utf-8'), headers=None)
        return res, content.decode('utf-8')
