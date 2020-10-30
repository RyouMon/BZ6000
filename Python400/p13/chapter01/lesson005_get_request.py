# GET 请求
# 传递查询参数
# 最后修改时间：2020/10/30

from urllib.request import Request, urlopen
from urllib.parse import urlencode


args = {
    'wd': '花泽香菜'
}
base_url = 'https://www.baidu.com/s?{}'
url = base_url.format(urlencode(args))
print(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58',
}

request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())
