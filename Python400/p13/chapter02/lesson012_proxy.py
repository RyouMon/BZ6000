# 使用代理
# 最后修改时间：2020/10/30

from urllib.request import Request
from urllib.request import build_opener
from urllib.request import ProxyHandler
from fake_useragent import UserAgent


url = 'http://httpbin.org/get'

headers = {
    'User-Agent': UserAgent().chrome,
}


request = Request(url)

handler = ProxyHandler({'http': 'host:port'})
opener = build_opener(handler)

response = opener.open(request)

print(response.read().decode())
