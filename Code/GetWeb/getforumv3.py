# -*- coding:utf-8 -*-

#20161029

import os
import re
import urllib
import urllib2
from bs4 import BeautifulSoup


#要爬取的网址
filename = "aaa.txt"
itemname = "div"
itemprop = {"class":"t_fsz"}
strlist = ["1"] + [str(i) for i in range(2,7)]
urlraw = "http://www.pdawiki.com/forum/thread-18615-%s-1.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}

urllist = [urlraw % str(u) for u in strlist]

def parsesoup(soup):
    [x.extract() for x in soup.find_all('span',attrs={'style':"display:none"})]
    [x.extract() for x in soup.find_all('font',attrs={'class':"jammer"})]


#爬取网页
def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request,timeout=20)
    return u_open.read()

#保存文件为txt
def writefile(name, fs):
    with open(name, "a") as f:
        f.write(fs)

def getfilepath(url):
    if ":" not in url: url = "../" + url
    u_r = urlraw.split("/")
    u = url.split("/")
    if u[0] == "..":
        while u[0] == "..":
            print u_r.pop(),u.pop(0)
        url = "/".join(u_r[:-1]+u)
    elif u[0] == ".":
        url = "/".join(u_r[:-1]+u[1:])
    elif u[0] == "":
        url = "/".join(u_r[:3]+u)
    return url

#保存文件
def getInfoFromContent(content):   
    imgs = content.find_all('img')
    fl = []
    for link in imgs:  
        url = link.get('src')
        #处理相对路径
        if not url: return [] 
        url = getfilepath(url)
        #url = url if u_r == urlraw.split("/") else "/".join(u_r[:-1]+u)
        filename = str(hash(url))+ "_" + url.split("/")[-1]
        urllib.urlretrieve(url, filename)
        print(link.get('src'))
        fl.append(filename)
    return fl

def getcontent(newsurl,itemname, itemprop):
    gethtml = url_request(newsurl,headers)
    #print ipchtml
    bs = BeautifulSoup(gethtml,"html.parser")
    html_find = bs.find_all(itemname ,attrs=itemprop)
    print len(html_find)
    #print news.text()

    ret_list = []
    for n in html_find:
        fl = getInfoFromContent(n) #get file
        parsesoup(n) #extact some text
        content = n.text.encode("utf8")
        content = re.sub(r' +',' ',content)
        content = re.sub(r'[\n]+','\n',content)
        ret_list.append(content)

    return ret_list


def parsecontent(content):
    c_str = [str(i) for i in content]
    return "\n".join(c_str)


#处理网页
for u in urllist:
    print u
    c_list = getcontent(u,itemname,itemprop)
    c = parsecontent(c_list)
    writefile(filename,"\n"+u+"\n")
    writefile(filename,c)
