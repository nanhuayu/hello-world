def mergesort(m):
    '''Merge Sort'''
    if len(m) <= 1:
        return m
    else:
        middle = len(m)/2
        left = m[:middle]
        right = m[middle:]

        left = mergesort(left)
        right = mergesort(right)
        return merge(left,right)

def merge(left, right):
    result = []
    leftidx,rightidx = 0,0
    while leftidx < len(left) and rightidx < len(right):
        if left[leftidx] <= right[rightidx]:
            result.append(left[leftidx])
            leftidx += 1
        else:
            result.append(right[rightidx])
            rightidx += 1

    for i in left[leftidx:]:
            result.append(i)
    for j in right[rightidx:]:
            result.append(j)

    return result

listtest = [1,24,35,78,9,2,35,63,6,7,43]
print mergesort(listtest)

