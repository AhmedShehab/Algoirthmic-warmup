import sys

def binary(a, x): 
    low = 0
    high = len(a) - 1
    mid = 0
  
    while low <= high: 
        mid = (high + low) // 2
        if a[mid] < x: 
            low = mid + 1
        elif a[mid] > x: 
            high = mid - 1
        else: 
            return mid 
    return -1
  
  
input = sys.stdin.readline()
data = list(map(int, input.split()))
n = data[0]
a = data[1:n+1]
input2 = sys.stdin.readline()
data2 = list(map(int, input2.split()))
n = data2[0]
b = data2[1:n+1]
for x in b:
    print(binary(a,x), end=' ')
