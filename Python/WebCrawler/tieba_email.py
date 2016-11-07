#!usr/bin/env python
# -*- coding:utf-8 -*-

#时间：2016年3月8日
#内容：爬取贴吧邮箱

import re
import urllib

i = 0
endpage = ""
emailurl = []

#备注：该网址已不存在/重新输入网站即可
urls = "http://tieba.baidu.com/p/3917222868?pn=%s"#%s 字符串
urls = "http://tieba.baidu.com/p/2314539885?pn=%s"

#正则表达式获取邮箱地址
def email(html):
    reg = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    reg = re.compile(reg)
    return re.findall(reg,html)

#打开并读取html文件
def openhtml(url):
    html = urllib.urlopen(url).read()
    return html

#通过打开尾页读取一共有多少网页
def emails(url):
    html = openhtml(urls)
    #print(html)
    reg = r'<a href="/p/.+?\?pn=(.+?)">尾页</a>'
    reg = re.compile(reg)
    endpage = re.findall(reg,html)[0]
    return endpage

#开始爬取
while 1:
    i += 1
    end = int(emails(urls))
    if i<=end:
        print("正在爬取第"+ str(i)+"页内容,总共%s页" %end)
        html = openhtml(urls %i)
        emailurl += email(html)
        #print(emailurl)
    else:
        break
f = open('url.txt',"a+")#a代表追加，如果没有该文件就创建
for i in emailurl:
    f.write(i+"\n")
f.close()
print("总共爬取到%s个邮箱地址" %len(emailurl))


