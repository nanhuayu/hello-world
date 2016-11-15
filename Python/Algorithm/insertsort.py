def insertsort(lists):
    '''insert_sort'''
    
    count = len(lists)
    for i in range(1,count):
        keys = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > keys:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1

            return lists
