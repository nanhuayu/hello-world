num = [0,0]

def getline(getnum):
    data = raw_input().split()
    getnum[0],getnum[1] = int(data[0]),int(data[1])
    return True

if getline(num):
    print num[0]+num[1]
