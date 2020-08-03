def minco(a,n):
    coins=[4,3,1]
    minNum=[None]*(n+1)
    minNum[0]=0
    options=[None]*3
    for i in range(1,len(a)):
        for j in range(0,len(coins)):
            if i >= coins[j]:
                options[j]=minNum[i-coins[j]]
            elif i<coins[j]:
                options[j]=i
            elif i ==coins[j]:
                return 1
        get = min(options)
        options=[None]*3
        minNum[i]=get+1
    return minNum[n]


n= int(input())
a=[]
for i in range(0,n+1):
    a.append(i)
print(minco(a,n))
