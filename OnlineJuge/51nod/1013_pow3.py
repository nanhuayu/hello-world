# -*- coding: utf-8 -*-
#2016/10/29

a = int(raw_input()) + 1
#print ((3 ** (a+1)-1) / 2)% 1000000007*2
r = 1
a_bin = str(bin(a))[::-1][:-2]
exp3 = [3]
for i in range(len(a_bin)):
    exp3.append(exp3[-1]**2 % (1000000007 * 2))
for i in range(len(a_bin)):
    if a_bin[i] == '1': r = r * exp3[i]
print(r - 1) // 2 % 1000000007
