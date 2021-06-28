import random
import time

def BubbleSort(mylist):
    swapflag = True
    while swapflag == True:
        swapflag = False
        n = len(mylist)
        for i in range (n-1):
            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                swapflag = True
    print(mylist)


def InsertionSort(mylist):
    n = len(mylist)
    for i in range (1, n):
        key = mylist[i]
        j = i
        while j > 0 and mylist[j-1] > key:
            mylist[j] = mylist[j-1]
            j = j-1
        mylist[j] = key
    print(mylist)


def SelectionSort(mylist):
    n = len(mylist)
    for i in range(n-1):
        min = i
        for j in range (i + 1, n):
            if mylist[j] < mylist[min]:
                min = j
        mylist[i], mylist[min] = mylist[min], mylist[i]
    print(mylist)  


def QuickSort(mylist):
    if mylist == []:
        return []
    pivot = random.choice(mylist)
    try:
        mylist.remove(pivot)
        mylist.insert(0, pivot)
    except ValueError:
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


if __name__ == "__main__": 
    
    mylist = random.sample(range(10, 100000), 1000)
    
    start = time.perf_counter()
    BubbleSort(mylist)
    elapsed = time.perf_counter() - start
    print(f"Bubble Sort executed in {elapsed:0.2f} seconds.") 


    start = time.perf_counter()
    SelectionSort(mylist)
    elapsed = time.perf_counter() - start
    print(f"Selection Sort executed in {elapsed:0.2f} seconds.")


    start = time.perf_counter()
    InsertionSort(mylist)
    elapsed = time.perf_counter() - start
    print(f"Insertion Sort executed in {elapsed:0.2f} seconds.")


    start = time.perf_counter()
    print(QuickSort(mylist))
    elapsed = time.perf_counter() - start
    print(f"Quick Sort executed in {elapsed:0.2f} seconds.")
    
    start = time.perf_counter()
    print(MergeSort(mylist))
    elapsed = time.perf_counter() - start
    print(f"Merge Sort executed in {elapsed:0.2f} seconds.") 
