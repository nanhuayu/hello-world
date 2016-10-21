'''
from itertools import permutations
print list(permutations('12345'))
'''

def permutation(s):
    ql = []
    if len(s)<2:
        ql.append(s)
    else:
        ql.append(s[0])
        
        for i in s[1:]:
            
            qlnew = []
            #print i
            for q in ql:
                #print q
                for l in range(len(q)+1):
                    #print l
                    temp = list(q)
                    temp.insert(l,i)
                    qlnew.append("".join(temp))
            ql = qlnew
        
    return ql
        
s = raw_input()
ql = sorted(set(permutation(s)))
print "\n".join(ql)
