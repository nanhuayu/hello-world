# -*- coding:utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup

import smtplib
from email.mime.text import MIMEText
from email.header import Header


#要爬取的网址
url = 'http://swgk.ipc.ac.cn/info_www/news/detailnewsb.asp?infoNo=13681'
listurl = 'http://swgk.ipc.ac.cn/Info_www/news/ColumnIndex.asp?columncode=021'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}

#爬取网页
def url_request(u, h):
    u_request = urllib2.Request(u,headers = h)
    u_open = urllib2.urlopen(u_request,timeout=20)
    u_read = u_open.read()
    return u_read

def writefile(name,t):
    with open(name,"w") as f:
        f.write(t)

def getlist(listurl):
    ipchtml = url_request(listurl,headers)
    #print ipchtml
    bs = BeautifulSoup(ipchtml,"html.parser")
    news = bs.find_all("div",align="center")
    #print news[1]
    bsnews = BeautifulSoup(str(news[1]),"html.parser")
    nl = bs.find_all("a",href=re.compile("infono="))
    for l in nl:
        print l.get("href")
    print len(nl)

def getnews(newsurl):
    ipchtml = url_request(newsurl,headers)
    #print ipchtml
    bs = BeautifulSoup(ipchtml,"html.parser")
    news = bs.find_all("table",class_="bgc_white")
    title = bs.find_all("title")[0].text.encode("utf8")
    #print news.text()
    num = re.search('infoNo=(.+)$',url)
    name = num.group()[7:] + ".txt"
 
    for n in news:
        content = n.text.encode("utf8")
        content = re.sub(' ','',content)
        content = re.sub('[\n]+','\n',content)
        writefile(name,content)

    return (title,content)

title,content = getnews(url)

#######################################################

m_host="smtp.163.com"  #设置服务器
m_sender="nanhuaboya@163.com"    #用户名
m_receiver="nanhuayu@qq.com"
m_pass="9930090193Nanhua"   #口令 
title = title
content = content

def sendmail(m_host,m_sender,m_receiver,m_pass,title,content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(title, 'utf-8')
    message['From'] = Header(m_sender)
    message['To'] =  Header(m_receiver)

    try:
        smtp = smtplib.SMTP_SSL() 
        smtp.connect(m_host)    # 25 为 SMTP 端口号
        smtp.set_debuglevel(1)
        smtp.login(m_sender,m_pass)
        smtp.sendmail(m_sender, m_receiver, message.as_string())
        print "Mail success!"
    except smtplib.SMTPException, e:
        print "Error: Unable to send mail......"
        print e
    finally:
        smtp.quit()

sendmail(m_host,m_sender,m_receiver,m_pass,title,content)
