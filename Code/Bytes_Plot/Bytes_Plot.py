with open('Untitled-1.c.exe','rb') as f:
  a= f.read()

chart = [0]*256
for i in a:
 chart[i]+=1

with open('chart.txt','w',encoding="utf8") as f:
 f.write(str(chart))

from pylab import *

plot(chart)
show()
