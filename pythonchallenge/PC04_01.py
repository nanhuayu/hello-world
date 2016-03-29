# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import os

"""
http://www.pythonchallenge.com/pc/def/linkedlist.php
"""
def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request)
    u_read = u_open.read()
    return u_read

def chuangguan():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=41423'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
    
    a = re.search('is [\d]+',url_request(url,headers)).group(0)
    urlnew = url[:-5] + a[3:]
    print a[3:]
    while url_request(urlnew,headers):
        b = re.search('is [\d]+',url_request(urlnew,headers)).group(0)
        urlnew = url[:-5] + b[3:]
        print b[3:]


chuangguan()
