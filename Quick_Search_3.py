import sys 
import random

def partition(a,l,r):
    pivot= a[l]
    count=l
    for i in range (l+1,r+1):
        if a[i]<pivot:
            count+=1
            a[i],a[count]=a[count],a[i]
    a[count],a[l]=a[l],a[count]
    temp=count
    for i in range(count,r+1):
        if a[i]==pivot:
            if temp!=i:
                a[temp],a[i]=a[i],a[temp]
            temp+=1
    return count,temp-1

def quick(a,l,r):
    if l>r:
        return 
    k = random.randint(l,r)
    a[l],a[k]=a[k],a[l]
    m,y=partition(a,l,r)
    quick(a,l,m-1)
    quick(a,y+1,r)
    return a

input=sys.stdin.read()
n,*a=map(int,input.split())
a= quick(a,0,len(a)-1)
for x in a:
    print(x, end=' ')
