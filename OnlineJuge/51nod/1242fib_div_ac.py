"""
fi,fj = 1,1
for i in range(1,s):
    fi, fj = fj %1000000009, (fi+fj)%1000000009
"""

MOD = 1000000009

def mm(a, b):
    c = [[0,0],[0,0]]
    c[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0])%MOD
    c[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1])%MOD
    c[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0])%MOD
    c[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1])%MOD
    return c

def mp(p, n):
    if n == 1:
        return p
    tmp = mp(p, n>>1)
    ans = mm(tmp, tmp)
    if n & 1:
        ans = mm(ans, p)
    return ans

def fib(n):
    if n < 2:
        return 1
    m = [[0,1],[1,1]]
    fm = mp(m, n-1)
    return fm[1][1]

for i in range(1,10):
    print fib(i)
    
