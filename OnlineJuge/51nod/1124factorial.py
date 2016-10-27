# -*- coding: utf-8 -*-
#2016/10/21

#对于234689算出n次方尾数
def num_last(val, n):
    res = 1
    n_tmp = []
    val_tmp = [val]
    while n >= 1:
        n_tmp.append(n%10)
        val_tmp.append(val_tmp[-1]**10 % 10)
        n /= 10
    #print n_tmp, val_tmp
    
    for i in range(len(n_tmp)):
        res *= val_tmp[i] ** n_tmp[i] % 10
        #print res
    return res % 10

#按mod(10)把数字拆分成1234689的n次方
def num_split(num):
    res = [0,0,0,0,0,0,0,0,0,0]
    #res_five = []
    while num >= 1:
        #res_five.append(num%5)
        for i in range(10):
            res[i] += num / 10
        for i in range(num%10):
            res[i] += 1
        num /= 5
    #print res_five,res_tmp
    #print res
    return res
    

fac_list = num_split(int(raw_input()))
res_list = []
fac_list[2-1] -= fac_list[5-1]
fac_list[6-1] -= fac_list[10-1]
fac_list[3-1] += fac_list[10-1]
for i in range(9):
    res_list.append(num_last(i+1,fac_list[i]))

res = (res_list[1]*res_list[2]*res_list[3]*res_list[5]*res_list[6]*res_list[7]*res_list[8])%10
print res
