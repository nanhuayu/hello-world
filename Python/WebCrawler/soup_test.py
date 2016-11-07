# -*- coding: utf-8 -*-

#测试bs包的使用
from bs4 import BeautifulSoup

#要爬取的网址内容
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc,'html.parser')

print soup.title
print soup.title.name
print soup.title.string
print soup.p
print soup.a
print soup.find_all('a')
print soup.find(id='link3')
print soup.get_text()
print soup.find_all('a')[0].get_text()
