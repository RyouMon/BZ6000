# BeautifulSoup4 的使用
# 获取起点中文网全部作品第一页的所有标题和作者
# 最后修改时间：2020/11/04

import requests
from bs4 import BeautifulSoup


url = 'https://www.qidian.com/all'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56',
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

all = soup.select('.book-mid-info')

for story in all:
    title = story.h4.a.text
    author = story.find(class_='author').find(class_='name').text
    print(title, ' by ', author)

