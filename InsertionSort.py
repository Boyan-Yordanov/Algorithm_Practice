def InsertionSort(mylist):
    n = len(mylist)
    for i in range (1, n):
        key = mylist[i]
        j = i
        while j > 0 and mylist[j-1] > key:
            mylist[j] = mylist[j-1]
            j = j-1
        mylist[j] = key
    return(mylist)


if __name__ == '__main__':                
    mylist = [1, 15, 2, 6, 8, 33, 555, 777, 65, 3]
    print (InsertionSort(mylist))
