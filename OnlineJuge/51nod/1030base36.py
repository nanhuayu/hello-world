# -*- coding: utf-8 -*-
#2016/10/28

a = raw_input()
a_len = len(a)
num36 = [ord(i) for i in a]
for i in range(a_len):
    if num36[i]> 64:num36[i] -= 55
    else:num36[i] -= 48
    num36[i] *= 36 ** (a_len - i - 1)
print sum(num36)

"""
print int(raw_input(), 36)
"""