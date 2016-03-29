# -*- coding:utf-8 -*-
import urllib
import zipfile
import re

'''
http://www.pythonchallenge.com/pc/def/channel.html
'''

def matchfile(t):
    s = re.search('is ([0-9]+)', t)
    if s:
        return s.group(1)
    else:
        print t
    
z = zipfile.ZipFile('channel.zip','r')
answer = ''
nums = '90052'

while nums:
    fn = nums + '.txt'
    text = z.read(fn)
    nums = matchfile(text)
    answer += z.getinfo(fn).comment

print answer 


'''
for f in z.namelist():
    text = z.read(f)
    print text
'''
'''
fn = nums + '.txt'
text = z.read(fn)
print text
nums = matchfile(text)
print nums
answer += z.getinfo(fn).comment
print answer

'''
