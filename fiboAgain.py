# Uses python3
def fib(n):
    f = [0, 1]
    for i in range(2, n+1):
        temp = f[i-1] + f[i-2]
        f.append(temp)
    return f[n]

def pisano(m): 
    a, b = 0, 1
    c=a+b
    for i in range(0, m * m): 
        c= (a+b)%m 
        a=b
        b=c
         
        if (a == 0 and b == 1): 
            return i + 1


def fibmod(n,m):
    temp = n%pisano(m)
    return fib(temp)%m

n , m = map(int, input().split())
print(fibmod(n,m))