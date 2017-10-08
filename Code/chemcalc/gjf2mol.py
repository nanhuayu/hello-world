# coding: utf-8

import sys

print(sys.argv)
filename = sys.argv[1]
with open(filename, 'r',encoding='utf8') as f:
    tmpstr = f.read()

molstr = tmpstr.split("\n\n")[2]
molstrlist = [[j for j in i.split(" ") if j] for i in molstr.split('\n') if i][1:]

#print(molstr)
#[print(i) for i in molstrlist[:5]+molstrlist[-1:]]

molnamelist = dict()
for i in range(len(molstrlist)):
    if molstrlist[i][0] in molnamelist:
        molnamelist[molstrlist[i][0]].append(i)
    else:
        molnamelist[molstrlist[i][0]]=[i]

print(molnamelist)

def getlist(listname):
    count = len(molnamelist[listname])
    retlist = ["  ".join(molstrlist[i]) for i in molnamelist[listname] ]
    return count, retlist


dalheadstr = "BASIS\n3-21G\n{0}\n------------------------\nAtomTypes={1} NoSymmetry Angstrom\n"
with open(filename[:-4]+".mol",'w',encoding='utf8') as f:
    f.write(dalheadstr.format(filename[:-4],len(molnamelist)))
for i in molnamelist:
    #print(i)
    count, atomstr = getlist(i)
    with open(filename[:-4]+".mol",'a',encoding='utf8') as f:
        f.write("Charge={0} Atoms={1}\n".format(i,count))
        f.write("\n".join(atomstr) + "\n")
    



