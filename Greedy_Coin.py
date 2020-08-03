# Uses python3

def number(m):
    count=0
    while m>0:
        if m>=10:
            m-=10
            count+=1
        elif m>=5:
            m-=5
            count+=1
        elif m>=1:
            m-=1
            count+=1
    return count

m = int(input())
print(number(m))
