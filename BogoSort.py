import random

def BogoSort(mylist):
    while(is_sorted(mylist) == False):
        shuffle(mylist)
    return(mylist)

def is_sorted(mylist):
    n = len(mylist)
    for i in range(0, n-1):
        if (mylist[i] > mylist[i+1]):
            return False

def shuffle(mylist):
    n = len(mylist)
    for i in range (0, n):
        r = random.randint(0, n-1)
        mylist [i], mylist[r] = mylist[r], mylist[i]


if __name__ == '__main__':       
    mylist = [1, 15, 2, 6, 8, 33, 555, 777, 65, 3]
    print (BogoSort(mylist))
