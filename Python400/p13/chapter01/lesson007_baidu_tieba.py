# 练习爬取百度贴吧
# 最后修改时间：2020/10/30

from urllib.request import Request, urlopen
from urllib.parse import quote


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58',
}


def get_html(url):
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read().decode()


def save_html(html, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


def main(pages, content):
    kw = quote(content)
    for pn in range(int(pages)):
        url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(kw, pn*50)
        html = get_html(url)
        save_html(html, 'baidu-[{}]'.format(pn))


if __name__ == '__main__':
    content = input('请输入要获取的贴吧：')
    pages = input('请输入要获取的页数：')
    main(pages, content)
