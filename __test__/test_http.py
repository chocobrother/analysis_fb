#http testing

import sys
from urllib.request import Request, urlopen
from datetime import *
try:
    url = "http://192.168.1.30:8080/mysite3/guestbook/ajax"
    request = Request(url)
    resp = urlopen(request)

    print(resp)
    resp_body = resp.read().decode('utf-8')
    print(resp_body)
except Exception as e:
    print('%s : %s'%(e,datetime.now()), file = sys.stderr)

