# AJAX 请求
# 以豆瓣电影作为实例
# 最后修改时间：2020/10/30

from urllib.request import urlopen, Request
from time import sleep


base_url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start={}'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58'
}


def get_response(url):
    request = Request(url, headers=headers)
    return urlopen(request)


for t in range(3):
    url = base_url.format(t*20)
    response = get_response(url)
    print(response.read().decode())
    sleep(0.5)
