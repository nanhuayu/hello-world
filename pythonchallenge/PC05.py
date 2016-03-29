# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

"""
http://www.pythonchallenge.com/pc/def/peak.html
"""
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}

def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request)
    u_read = u_open.read()
    return u_read

import pickle
banner = url_request(url,headers)
bannernew = pickle.loads(banner)

for i in bannernew:
    print ''.join(x[0]*x[1] for x in i)
    
    """
    j = ''
    for x in i:
        j += x[0]*x[1]
    print j
    """
