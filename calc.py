def sep(steps):
    a=[]
    for i in steps[:]:
        a.append(i)
    return a
def mincalc(a,n):
    seq=[]
    seq.append((0,1))
    minNum=[None]*(n)
    options={}
    for i in a:
        if i == 1:
            minNum[i-1]=0
        else:
            if i % 3==0:
                options[3]=minNum[(i//3)-1]
            if i%2 ==0:
                options[2]=minNum[(i//2)-1]
            if (i-1)!=0:
                options[1]=minNum[(i-1)-1]
            get = min(options.values())
            minNum[i-1]=get+1
            for key,Value in options.items():
                if  get == Value:
                    x=key
                    break
            if x==3:
                b=sep(seq[(i//3)-1])
                b.append(i)
                seq.append((b))
            elif x==2:
                b=sep(seq[(i//2)-1])
                b.append(i)
                seq.append((b))
            elif x==1:
                b=sep(seq[(i-2)])
                b.append(i)
                seq.append((b))
        options={}
    print(minNum[n-1])
    seq[i-1].pop(0)
    return seq[n-1]


n= int(input())
a=[]
for i in range(1,n+1):
    a.append(i)
print(*mincalc(a,n), sep=" ")