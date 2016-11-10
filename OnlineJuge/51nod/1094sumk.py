# -*- coding: utf-8 -*-
#2016/10/28
#一整数数列a1, a2, ... , an（有正有负），以及另一个整数k
#求一个区间[i, j]，(1 <= i <= j <= n)，使得a[i] + ... + a[j] = k。

x,k = (int(i) for i in raw_input().split())
a_list = [int(raw_input()) for i in range(x)]

#print a_list
#a_list = [1,2,3,4,5,6]

def sum_k():
    for a in range(len(a_list)):
        a_sum = a_list[a]
        for b in range(a+1,len(a_list)):
            a_sum += a_list[b]
            if a_sum == k:return [a+1,b+1]
            #if a_sum > k:break
    return False

res = sum_k()
if res:print res[0],res[1]
else:print "No Solution"
