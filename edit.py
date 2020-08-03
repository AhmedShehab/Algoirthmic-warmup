import sys


def comp(w1,w2):
    dist={}
    dist[0,0]=0
    for i in range(1,len(w1)):
        dist[i,0]=i
        for j in range(1,len(w2)):
            dist[0,j]=j
            if w1[i]==w2[j]:
                dist[i,j]= dist[i-1,j-1]
            else:
                dist[i,j]=1+min(dist[i-1,j-1],dist[i,j-1],dist[i-1,j])
    return dist[i,j]


w1="0"+input()
w2="0"+input()
print(comp(w1,w2))