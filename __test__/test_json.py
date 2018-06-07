# JSON Test

import sys
from urllib.request import Request, urlopen
from datetime import *
import json
try:
    url = "http://192.168.1.30:8080/mysite3/guestbook/api/list"
    request = Request(url)
    resp = urlopen(request)

    resp_body = resp.read().decode('utf-8')
    json_result = json.loads(resp_body)
    print(resp_body)
    print(type(resp_body))
    print(json_result)
    print(type(json_result))
except Exception as e:
    print('%s : %s'%(e,datetime.now()), file = sys.stderr)

