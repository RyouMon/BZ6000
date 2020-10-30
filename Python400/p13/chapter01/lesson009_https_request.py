# HTTPS 请求的证书问题
# 使用 ssl 忽略证书问题
# 最后修改时间：2020/10/30

from urllib.request import urlopen, Request
import ssl


url = 'https://www.yangfenzi.com/tag/zhengfu'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58',
}


request = Request(url, headers=headers)

context = ssl._create_unverified_context()
response = urlopen(request)
print(response.read().decode())
