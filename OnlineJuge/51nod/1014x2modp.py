# -*- coding: utf-8 -*-
#2016/10/21

m, r = (int(i) for i in raw_input().split())
a = [(i+1)**2 % m for i in range(m-1)]
a_index = [str(i+1) for i in range(len(a)) if a[i] == r]
if len(a_index):print ' '.join(a_index)
else:print "No Solution"
