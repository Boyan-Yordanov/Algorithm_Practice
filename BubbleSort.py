def swap (mylist, item1, item2):
    mylist[item1], mylist[item2] = mylist[item2], mylist[item1]
    return (mylist)
  
def BubbleSort(mylist):
    swapflag = True
    while swapflag == True:
        swapflag = False
        n = len(mylist)
        for i in range (n-1):
            if mylist[i] > mylist[i+1]:
                mylist = swap(mylist, i, i+1)
                ''' For Infunction Swap '''
                # mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                swapflag = True
    return (mylist)


if __name__ == '__main__':
    mylist = [1, 15, 2, 6, 8, 33, 555, 777, 65, 3]
    print (BubbleSort(mylist))
