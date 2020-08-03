# Uses Python 3


def Max(a,b):
    count =0
    for i in range(0,n):
        count+=(a[i]*b[i])
   
    return count






n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
print(Max(a,b))