import random

def QuickSort(mylist):
    if mylist == []:
            return []
    pivot = random.choice(mylist)
    try:
        mylist.remove(pivot)
        mylist.insert(0, pivot)
    except ValueError:
        print("You have a Value Error!")
        pass
    less = []
    greater = []
    n = len(mylist)
    for i in range(1, n):
        if mylist[i] < pivot:
            less.append(mylist[i])
        else:
            greater.append(mylist[i])
    return(QuickSort(less) + [pivot] + QuickSort(greater))


if __name__ == '__main__':
    mylist = [1, 15, 2, 6, 8, 33, 555, 777, 65, 3]
    print (QuickSort(mylist))
