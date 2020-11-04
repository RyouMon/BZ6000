# 使用正则表达式匹配糗事百科的段子
# 最后修改时间：2020/11/01

import re
import requests


url = 'https://www.qiushibaike.com/text/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56',
}

response = requests.get(url, headers=headers)

pattern = r'<div class="content">\s<span>\s*(.*)\s'

contents = re.findall(pattern, response.text)

for content in contents:
    print(content, '\n')
