# -*- coding: utf-8 -*-
#2016/10/21

def in_bisect(oneword,t):
    """search word list in bisect."""
    head = 0
    tail = len(t)-1
    while head <= tail:
        if oneword > t[(head + tail)/2]:
            head = (head + tail)/2+1
        elif oneword < t[(head + tail)/2]:
            tail = (head + tail)/2-1
        else:
            #print (head + tail)/2
            return (head + tail)/2
    #print head
    return head


num_list = [5**i*3**j*2**k for i in range(26) for j in range(38-int(i*1.46)) for k in range(60-int(i*2.32)-int(j*1.58))]

num_list.sort()
num = int(raw_input())
for i in range(num):
    num_n = int(raw_input())
    if num_n < 3:print 2
    else:print num_list[in_bisect(num_n,num_list)]

#print len(num_list)
#print ' '.join([str(num_list[i]) for i in range(20)])