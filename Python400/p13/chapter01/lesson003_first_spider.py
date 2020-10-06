"""
使用 urllib.request 进行 URL 请求
"""
from urllib.request import urlopen


url = 'http://www.baidu.com'

# 使用urlopen()函数打开一个URL，得到一个http.client.HTTPResponse对象
response = urlopen(url)

print(type(response))

# 获取HTML
html = response.read().decode()
print(html)

# 获取状态码
print(response.getcode())

# 获取实际请求的URL
print(response.geturl())

# 获取响应头信息
print(response.info())
