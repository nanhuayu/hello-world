from pylab import *
import sys

with open(sys.argv[1],'r',encoding='utf8') as f:
    tmpstr = f.read()

molstr = tmpstr.split("\n\n")[2]

molstrlist = [[j for j in i.split(" ") if j] for i in molstr if i]

for i in molstrlist[1:]:
    if i[0]

eigenvirtlist = [i.split("--")[-1].split(" ") for i in eigenstr.split('\n') if i and "Alpha virt. eigenvalues --" in i]
eigenvirtval = [float(val) for i in eigenvirtlist for val in i if val]

print(eigenoccval[-10:] + eigenvirtval[:10])
plot([i-9 for i in range(20)],eigenoccval[-10:] + eigenvirtval[:10])
show()
