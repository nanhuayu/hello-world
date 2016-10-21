MOD = 1000000009
s = int(raw_input())

fi,fj = 1,1
for i in range(1,s):
    fi, fj = fj %MOD , fi+fj %MOD

print fi
    
