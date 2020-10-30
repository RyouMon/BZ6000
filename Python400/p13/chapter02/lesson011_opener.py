# Opener 的使用
# 最后修改时间：2020/10/30
from urllib.request import Request, build_opener, HTTPHandler
from fake_useragent import UserAgent


url = 'http://httpbin.org/get'

headers = {
    'User-Agent': UserAgent().chrome,
}

request = Request(url, headers=headers)

handler = HTTPHandler(debuglevel=1)
opener = build_opener(handler)
response = opener.open(request)

print(response.read().decode())
