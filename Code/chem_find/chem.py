#coding:utf-8

import re

with open("test.html","r") as c:
    txt = c.read()

a = re.findall(">*[0-9]+-[0-9]+-[0-9]+<*",txt)
for i in a:
    #print i
    with open("chem_all.txt","a") as c:
        c.write(i)
