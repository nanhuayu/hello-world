#-*-encoding:utf-8-*-

#时间：2016年4月19日
#内容：爬取网页图片

import json
import urllib

#文件保存在youdaotemp.txt中/格式为json
#把其中image标签下的网址保存并下载
f = file(r'youdaotemp.txt')
jsonobj = json.load(f)
count = 0
img = 0
for i in jsonobj:
    count += 1 

    if 'image' in i:
        img += 1
        
        path = r'%s.jpeg'%i['date']
        urllib.urlretrieve(i['image'], path)
        
    '''
    print i['date']
    print i['sen']
    print i['trans']
    '''
print img
print count
f.close
