import sys

def major(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left + right - 1)//2
    lhalf = major(a, left,mid  + 1)
    rhalf = major(a, mid + 1, right)
    left_count = 0
    right_count = 0
    for i in a[left:right]:
        if i == lhalf:
            left_count += 1
        if i == rhalf:
            right_count += 1
    if right_count > (right-left)//2:
        return rhalf
    if left_count > (right-left)//2:
        return lhalf

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if major(a, 0, len(a)) != -1:
        print(1)
    else:
        print(0)
