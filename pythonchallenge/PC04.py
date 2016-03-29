# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

"""
http://www.pythonchallenge.com/pc/def/linkedlist.php
"""
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}

def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request)
    u_read = u_open.read()
    return u_read

def next_page(n):
    urlnew = url + n
    text = url_request(urlnew,headers)
    m = re.search('is ([0-9]+)',text)
    if m:
        return m.group(1)
    else:
        print url_request(urlnew,headers)
        
nums = '12345'
nums = '8022'
nums = '63579'
while nums:
    print nums
    nums = next_page(nums)
