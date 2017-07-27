#coding:utf-8

import re

with open("chem_find.txt","r") as c:
    c_find = eval(c.read())

with open("chem_all.txt","r") as c:
    c_all = eval(c.read())


print set(c_find) & set(c_all)
