import sys

def getline():
    data = sys.stdin.readline().split()
    return [int(data[0]), int(data[1]), int(data[2])]

def minus(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    
def det(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
    
def plane(a, b, c, d):
    la = minus(a, b)
    lb = minus(a, c)
    lc = minus(a, d)
    return dot(det(la, lb), lc)
    
data = sys.stdin.readline().split()
T = int(data[0])

for k in range(T):
    if plane(getline(), getline(), getline(), getline()):
        print "Yes"
    else:
        print "No"
