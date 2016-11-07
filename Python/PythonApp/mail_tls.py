#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host="smtp-mail.xxx.com"  #设置服务器
mail_sender="sender@xxx.com"    #用户名
mail_receiver="receiver@xxx.com"
mail_pass="password"   #口令 
mail_subject = 'Hello, %s' %mail_receiver
mail_text="""\
Hello, %s:\n\
I'm from %s. \n\
Nice to meet you!\
""" %(mail_receiver,mail_sender)


message = MIMEText(mail_text, 'plain', 'utf-8')
message['Subject'] = Header(mail_subject, 'utf-8')
message['From'] = Header(mail_sender)
message['To'] =  Header(mail_receiver)

try:
    smtp = smtplib.SMTP() 
    smtp.connect(mail_host,587)    # 25 为 SMTP 端口号
    smtp.set_debuglevel(1)
    smtp.starttls()
    smtp.login(mail_sender,mail_pass)
    smtp.sendmail(mail_sender, mail_receiver, message.as_string())
    print "Mail success!"
except smtplib.SMTPException, e:
    print "Error: Unable to send mail......"
    print e
finally:
    smtp.quit()
