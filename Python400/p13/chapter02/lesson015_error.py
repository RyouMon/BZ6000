# 异常的捕获
# 最后修改日期：2020/10/31

from urllib.request import Request, urlopen
from urllib.error import URLError


url = 'http://www.baidu.com/sdfrfew/dfg'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56',
}

request = Request(url, headers=headers)

try:
    response = urlopen(request)
    print(response.read().decode())
except URLError as reason:
    print(reason)

print('finished')
