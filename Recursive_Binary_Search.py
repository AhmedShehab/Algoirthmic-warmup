import sys

def search(i,a,l,r):
    if l>r:
        return -1
    mid = (r+l)//2  
    if a[mid]==i:
        return mid
    elif a[mid]<i:
        return search(i,a,mid+1,r)
    elif a[mid]>i:
        return search(i,a,l,mid-1)
    else:
        return -1


input=sys.stdin.readline()
n,*a=map(int,input.split())
input2=sys.stdin.readline()
k,*b=map(int,input2.split())
for i in b:
    print(search(i,a,0,len(a)-1),end=" ")
