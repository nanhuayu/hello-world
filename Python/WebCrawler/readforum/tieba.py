# -*- coding:utf-8 -*-

#20161029

import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import os

#要爬取的网址
url = 'http://tieba.baidu.com/p/2511853162?pn=%s'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}

#爬取网页
def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request,timeout=20)
    return u_open.read()

#保存文件为txt
def savefile(fs, name):
    with open(name+".txt", "a") as f:
        f.write(fs)

"""
def url_catch():
    pass
"""

#对每日一句的内容进行分析并保存
def every(n):
    urlnew = url%str(n+1)
    print urlnew
    savefile(''.join(['\n',urlnew]),"tieba1")
    a = url_request(urlnew, headers)
    #print a
    soup = BeautifulSoup(a,'html.parser')
    b = soup.find_all("div",{"class":"d_post_content j_d_post_content "})
    print len(b)
    if len(b):
        for i in b:
            #print i.get_text()
            savefile('\n'.join(["\n",i.get_text().encode("gb18030").strip()]),"tieba1")
    else:pass

#大概有260个网页
for i in range(9):
    every(i)
