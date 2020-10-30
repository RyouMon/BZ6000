# Cookiejar 的使用
# 读取 Cookie
# 最后修改时间：2020/10/30

from urllib.request import Request
from urllib.request import build_opener, HTTPCookieProcessor
from http.cookiejar import MozillaCookieJar


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56',
}

url = 'http://www.rrys2020.com/user/user/'

cookiejar = MozillaCookieJar()
handler = HTTPCookieProcessor(cookiejar)
opener = build_opener(handler)

cookiejar.load('cookies.txt', ignore_discard=True, ignore_expires=True)

request = Request(url, headers=headers)
response = opener.open(request)
print(response.read().decode())
