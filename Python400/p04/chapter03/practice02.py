#!/usr/bin/env python
# -*-coding:utf-8-*-
import urllib.request
import re


response = urllib.request.urlopen('https://www.jitashe.org/')
text = response.read().decode()
pattern = r'<img.+?src="(.+?)"'
for url in re.findall(pattern, text):
    print(url)
