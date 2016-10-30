#
#20161029

a,b = (int(i) for i in raw_input().split())

def num_count(num):
    num_list = [int(i) for i in str(num)][::-1]
    count = [0,0,0,0,0,0,0,0,0,0]
    for idx in range(len(num_list)):
##        if idx == 0:
##            count[num % 10] += 1
        count = [x + (num / 10**(idx+1)) * 10**idx for x in count]
        for x in range(num / 10**idx % 10):
            count[x] += 10**idx
        count[num / 10**idx % 10] += num % 10**idx + 1
    count[0] -= (10 ** len(num_list) - 1)/9
    return count

count_a,count_b = num_count(a-1),num_count(b)
print count_a
print count_b

for i in range(10):
    print count_b[i]-count_a[i]
