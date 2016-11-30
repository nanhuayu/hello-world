#python challenge

#challenge00
2**38

#challenge01
"".join([chr((ord(i)-94)%26+96) if i.isalpha() else i for i in text])

#challenge02
def hist(i,h):
    if i in h.keys():h[i]+=1
    else:h[i]=1

for (key,value) in h.iteritems():
    print (key,value)

a = "".join([i if i.isalpha() for i in text])

#challenge03
