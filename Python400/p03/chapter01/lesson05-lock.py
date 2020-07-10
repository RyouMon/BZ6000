#!/usr/bin/env python
# -*-coding:utf-8-*-
#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
锁
"""
from threading import Thread
from threading import Lock


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        global count
        lock.acquire()
        for i in range(100000):
            count += 1
        lock.release()


if __name__ == '__main__':
    count = 0
    lock = Lock()
    for i in range(10):
        t = MyThread(i)
        t.start()
    print("count: {0}".format(count))
