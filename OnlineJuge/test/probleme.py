cow = [0,0,0,1]

def birth(cow):
    cow[3] = cow[3] + cow[2]
    cow[2] = cow[1]
    cow[1] = cow[0]
    cow[0] = cow[3]
    return cow

for i in range(50):
    birthcow = birth(cow)
    print i +1, ":", sum(birthcow),'\n    ', birthcow
