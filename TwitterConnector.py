import oauth2
import os.path
import json
import urllib.parse
from xml.etree import cElementTree


# Singleton pattern decorator
def singleton(cls: type, *args, **kw):
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

        self.__client = oauth2.Client(consumer, token)

    def __oauth_req(self, url: str, params: dict = None) -> (dict, str):
        # Add parameters to url
        if params is not None:
            url_parts = list(urllib.parse.urlparse(url))
            now_params = dict(urllib.parse.parse_qsl(url_parts[4]))
            now_params.update(params)
            url_parts[4] = urllib.parse.urlencode(now_params)
            url = urllib.parse.urlunparse(url_parts)

        res, content = self.__client.request(url, method='GET', body=''.encode('utf-8'), headers=None)
        return res, content.decode('utf-8')

    def get_json_res(self, url: str, params: dict = None):
        res, text = self.__oauth_req(url, params)
        if res['status'] == '200':
            return json.loads(text)
        else:
            raise RuntimeError('Http code: %s' % res['status'])
