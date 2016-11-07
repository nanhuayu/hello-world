# -*- coding:utf-8 -*-

#时间：2016年3月3日
#内容：爬取iciba每日一句的内容

import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import os

#要爬取的网址
url = 'http://news.iciba.com/dailysentence/detail-%s.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}


#爬取网页
def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request,timeout=20)
    u_read = u_open.read()
    return u_read

#保存文件为txt
def savefile(fs, name):
    f = open(name+".txt", "a")
    #line = f.readline()
    f.write(fs)
    f.close()

"""
def oneday(a):
    #a = url_request(url, headers)
    b = re.search('meta name="description" content="[^"]+"',a)
    print b
    c = b.group(0)
    
    savefile(c+"\n","every1")
"""
    
def everyday(n):

    for i in range(n):
        urlnew = url%str(i+1)
        print urlnew
        a = url_request(urlnew, headers)
        try:
            b = re.search('meta name="description" content="[^"]+"',a).group(0)
            print b
            savefile(b+"\n","every1")

        #如果没有对应网站/略过并继续爬取下一个网站
        except AttributeError, e:
            pass
            

everyday(1871)
