from urllib.parse import urlencode
from .json_request import json_request

BASE_URL_FB_API = 'https://graph.facebook.com/v3.0'
ACCESS_TOKEN = 'EAACEdEose0cBAK7QHgznSQV195ASStxILYCZCjSX3rX3ZAN03X4frH4OyZBpTH8CZAnsr9x1yjZCyAZABMcmYZBRlwlkQchxQRZAaUs5qZBQ9gLt4DVZCQf5jDx9QWZCAZBKxPNdy1HIKuozZCyfwvJWnLazh1VklKdvlGeddBYlbqYHzmpgRJXiZAZA1ZBRHu3oJwTTTvYPL9i3mAalWwZDZD'



def fb_gen_url(base=BASE_URL_FB_API, node='', **param):

    print('%s/%s/?%s' % (base, node, urlencode(param)))
    return '%s/%s/?%s' % (base, node, urlencode(param))



def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url)
    print(json_result)
    return json_result.get('id')

def fb_fetch_post(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename)+'/posts',
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN)



    isnext = True
    data = []
    while isnext is True:
        json_result = json_request(url=url)

        print(json_result)
        paging = None if json_result is None else json_result.get('paging')

        posts = None if json_result is None else json_result.get('data')
        url = None if paging is None else paging.get('next')

        isnext = url is not  None


        yield posts

        data += posts

        return data



fb_gen_url(pagename='jtbcnews', a=1,b=2,token='')
urlencode({'a':1,'b':2,'token': ''})