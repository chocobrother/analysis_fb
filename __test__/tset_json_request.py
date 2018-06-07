import sys
from  datetime  import datetime
from analysis_fb.collection.api import json_request as jr

url = "http://192.168.1.30:8080/mysite3/guestbook/api/list"


def success_fetch_guestbook_list(response):
    print(response)


def error_fetch_guestbook_list(e):
    print('%s : %s' % (e, datetime.now()), file=sys.stderr)


jr.json_request(url=url, success=success_fetch_guestbook_list)
"""
json_result = jr.json_request(url=url)

print(json_result)
"""

