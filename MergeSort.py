def MergeSort(mylist):
    n = len(mylist)
    if n <= 1:
        return mylist
    middle_index = n//2
    a = MergeSort(mylist[:middle_index])
    b = MergeSort(mylist[middle_index:])
    return Merge(a,b)

def Merge(a, b):
    output = [None] * (len(a) + len(b))
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            output[k] = a[i]
            i += 1
        else:
            output[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        output[k] = a[i]
        i +=1
        k +=1
    while j < len(b):
        output[k] = b[j]
        j +=1
        k +=1
    return output
    
    
if __name__ == '__main__':    
    mylist = [1, 15, 2, 6, 8, 33, 555, 777, 65, 3]
    print (MergeSort(mylist))
