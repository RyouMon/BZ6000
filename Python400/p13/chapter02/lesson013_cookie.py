# Cookie 的使用
# 最后修改时间：2020/10/30

from urllib.request import Request
from urllib.request import HTTPCookieProcessor, build_opener
from urllib.parse import urlencode


login_url = 'http://www.rrys2020.com/User/Login/ajaxLogin'
after_login = 'http://www.rrys2020.com/user/user/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56',
}

form = {
    'account': 'l1xxxxxxx@live.com',
    'password': '01xxxxxxxxx',
}


handler = HTTPCookieProcessor()
opener = build_opener(HTTPCookieProcessor)

request = Request(login_url, headers=headers)
response = opener.open(request, data=urlencode(form).encode())
print(response.read().decode())

request = Request(after_login, headers=headers)
response = opener.open(request)
print(response.read().decode())
