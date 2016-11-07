# -*- coding:utf-8 -*-

#时间：2016年4月19日
#内容：爬取有道每日一句

import urllib
import urllib2
import re
import os

#要爬取的网址
url = 'http://xue.youdao.com/w?page=%s&type=sentence'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}

#爬取网页
def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request,timeout=20)
    u_read = u_open.read()
    return u_read

#保存文件为txt
def savefile(fs, name):
    with open(name+".txt", "a") as f:
        f.write(fs)

"""
def url_catch():
    pass
"""

#对每日一句的内容进行分析并保存
def everyday(n):
    urlnew = url%str(n+1)
    print urlnew
    a = url_request(urlnew, headers)
    #print a
    b = re.findall('var datas = ([\s\S]*?\});',a)
    print len(b)
    if b <> []:
        for i in b:
            savefile(i+"\n","youdao1")
    else:
        pass

#大概有260个网页
for i in range(260):
    everyday(i)
