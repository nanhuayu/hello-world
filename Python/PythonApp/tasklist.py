import os
import re

with os.popen('tasklist /nh','r') as f:
    for eachline in f:
        temp = re.split(r'\s\s+|\t',eachline.strip())
        if len(temp) == 4:
            print temp
