# -*- coding: utf-8 -*-
#2016/10/28
#一整数数列a1, a2, ... , an（有正有负），以及另一个整数k
#求一个区间[i, j]，(1 <= i <= j <= n)，使得a[i] + ... + a[j] = k。

x,k = (int(i) for i in raw_input().split())
a_list = [int(raw_input()) for i in range(x)]
b_list = [0]
for a in a_list:
    b_list.append(b_list[-1] + a)

#a_list = [1,2,3,4,5,6]
def sum_k():
    for i in range(len(b_list)):
        if b_list[i] + k in b_list[i+1:]:
            return [i+1, b_list.index(b_list[i] + k)]
    return False

def same_k():
    for i in range(len(b_list)):
        if b_list[i] in b_list[i+1:]:
            return [i+1, i+1+b_list[i+1:].index(b_list[i])]
    return False

if k <> 0:res = sum_k()
else:res = same_k()
if res:print res[0],res[1]
else:print "No Solution"
