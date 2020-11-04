# XPATH 的使用
# 获取起点中文网全部作品第一页的所有标题和作者
# 最后修改时间：2020/11/04

import requests
from lxml import etree


url = 'https://www.qidian.com/all'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56',
}

response = requests.get(url, headers=headers)

tree = etree.HTML(response.text)

titles = tree.xpath('//div[@class="book-mid-info"]/h4/a/text()')
authors = tree.xpath('//p[@class="author"]/a[1]/text()')

for title, author in zip(titles, authors):
    print(title, ' by ', author)
