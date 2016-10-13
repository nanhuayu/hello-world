num = [0,0]

def getline(getnum):
    try:
        data = raw_input().split()
        #print "data: %s" %data
        getnum[0],getnum[1] = data[0],data[1]
        #print getnum
        return True
    except EOFError:
        return False

def pownum(num):
    pnum = int(num[1])
    if '.' in str(num[0]):
        cmpnum = str(num[0]).rstrip('0').strip().split('.')
        cmpnum[0] = '0' if not cmpnum[0] else cmpnum[0]
        cmpnum[1] = '0' if not cmpnum[1] else cmpnum[1]
    else:
        cmpnum = [str(num[0]),'0']

    if cmpnum[1] <> '0':
        cmpnumlen = len(cmpnum[1])
        compute = int(''.join(cmpnum))
        res = str(compute**pnum)

        if int(cmpnum[0]) == 0:
            return '.'+'0'*(pnum*cmpnumlen-len(res))+res
        else:
            return res[0:-pnum*cmpnumlen]+'.'+res[-pnum*cmpnumlen:]
        
    else:
        return str(int(cmpnum[0])**pnum)


##for line in iter(raw_input, ''):
##    getline(num,line)
##    print pownum(num)

while getline(num):
    print pownum(num)
    #print num
