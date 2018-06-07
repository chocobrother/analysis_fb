from analysis_fb.collection.api import api


#url = api.fb_gen_url(node='jtbcnews',a=1, b=2, no=10, token='12345')

#print(url)


#id = api.fb_name_to_id('jtbcnews')

#print(id)


#posts = api.fb_fetch_post('jtbcnews', '2018-04-01','2018-04-30')
#print(posts)

for posts in api.fb_fetch_post('jtbcnews', '2018-04-01','2018-04-30'):
    print(posts)


