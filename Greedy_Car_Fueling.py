# Uses Python 3
def Stops(stop,d,m):
    count = 0
    for i in range(0,n):
        if stop[i]<=m and stop[i+1]>m:
            count+=1
            stop = [x - stop[i]  for x in stop]
    if stop[n]>m:
        count=-1
    return count

d = int(input())
m = int(input())
n = int(input())
stop = list(map(int,input().split()))
stop.append(d)
print(Stops(stop,d,m))
