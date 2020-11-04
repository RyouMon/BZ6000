# requests 库的使用
# 最后修改时间：2020/10/31

import requests


# GET 请求
url = 'http://www.baidu.com'

response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)
