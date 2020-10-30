# 动态设置 User-Agent
# 最后修改时间：2020/10/30

from fake_useragent import UserAgent


ua = UserAgent()

for i in range(3):
    print(ua.chrome)

for i in range(3):
    print(ua.random)
