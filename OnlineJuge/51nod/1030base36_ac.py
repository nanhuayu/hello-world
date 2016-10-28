# -*- coding: utf-8 -*-
#2016/10/28

s1="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mp={}
for i in range(36):
    mp[s1[i]]=i
s=raw_input()
def f(a,b):
    if a+1==b:
        return mp[s[a]]
    c=(a+b)//2
    return f(a,c)*(36**(b-c))+f(c,b)
print(f(0,len(s)))