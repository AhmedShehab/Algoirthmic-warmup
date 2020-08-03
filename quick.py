# Uses python3
import sys
import random


def quick_sort3(a):
    if len(a)<=1:
        return a
    rand=random.randint(0,len(a)-1)
    Pivot = a.pop(rand)
    lower=[]
    upper=[]
    equal=[]
    for i in range(0 , len(a)):
        if a[i] < Pivot:
            lower.append(a[i])
        elif a[i]==Pivot:
            equal.append(a[i])
        elif a[i] >Pivot:
            upper.append(a[i])
    return quick_sort3(lower) +[Pivot] + equal + quick_sort3(upper)



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a= quick_sort3(a)
    for x in a:
        print(x, end=' ')
