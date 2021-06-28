def swap(mylist, item1, item2):
    mylist[item1], mylist[item2] = mylist[item2], mylist[item1]
    return (mylist)

def SelectionSort(mylist):
    n = len(mylist)
    for i in range(n-1):
        min = i
        for j in range (i + 1, n):
            if mylist[j] < mylist[min]:
                min = j
        swap(mylist, i ,min)
    return mylist

           
if __name__ == '__main__':
    mylist = [1, 15, 2, 6, 8, 33, 555, 777, 65, 3]
    print(SelectionSort(mylist))
