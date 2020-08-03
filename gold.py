import sys
def gold(a,n,weights):
    num={}
    num[0,0]=0
    for j in range(0,n+1):
        for i in a:
            if i==0 or weights[j]==0:
                num[i,j]=0
            elif i>=weights[j]:
                num[i,j]=max(num[i,j-1],weights[j]+num[i-weights[j],j-1])
            elif i<weights[j]:
                num[i,j]=num[i,j-1]
    return num[i,j]

w, n = map(int,input().split())
input1=sys.stdin.readline()
weights =list(map(int,input1.split()))
weights.insert(0,0)
a=[]
for i in range(0,w+1):
    a.append(i)
print(gold(a,n,weights))
