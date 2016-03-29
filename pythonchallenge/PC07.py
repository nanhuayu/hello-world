# -*- coding:utf-8 -*-
import urllib
import urllib2
import StringIO
from PIL import Image
import re

'''
http://www.pythonchallenge.com/pc/def/oxygen.html
'''
url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}

def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request)
    u_read = u_open.read()
    return u_read

img = Image.open(StringIO.StringIO(url_request(url,headers)))
w,h = img.size
print w,h
print img.getpixel((0,h//2))
s0 =  ''.join([chr(img.getpixel((i, h//2))[0]) for i in range(0,w,7)])
print s0

s1 = [105, 110, 116, 101, 103, 114, 105, 116, 121]
answer = ''.join([chr(x) for x in s1])
print answer

'''
s =  ''.join([chr(img.getpixel((i, h//2))[0]) for i in range(0,w,1)])
print  ''.join(re.findall('(.){5,7}',s))
'''
