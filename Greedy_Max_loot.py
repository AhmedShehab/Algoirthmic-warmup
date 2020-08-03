# Uses Python 3
import numpy as np

def solution(search,c,w):
    v=0
    for i in range(0,n):
        if search[i][2]<=c:
            v+=search[i][1]
            c-=search[i][2]
        elif search[i][2]>c:
            a=c/search[i][2]
            v+=a*search[i][1]
            c=0
    return v

n,c= map(int,input().split())
v =        [None]*n
w =        [None]*n
fraction = [None]*n
search= [] 
for i in range(0,n):
    v[i],w[i] =map(int,input().split())
    search.append((v[i]/w[i],v[i],w[i]))
search.sort(reverse=True)
print(solution(search,c,w))
