# POST 请求
# 使用 POST 请求处理登录
# 最后修改时间：2020/10/30

from urllib.request import Request, urlopen
from urllib.parse import urlencode


url = 'https://vcb-s.com/wp-login.php'

data = {
    'log': 'User',
    'pwd': 'PWD',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58'
}

request = Request(url, headers=headers)

response = urlopen(request, data=urlencode(data).encode())

print(response.read().decode())
