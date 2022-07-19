def average():
    total = 0
    for i in range(1, len(arr)):
        total += arr[i]
    return total / num

def ratio():
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] > ave:
            cnt += 1
    return (cnt / num) * 100

C = int(input())

for tc in range(C):
    arr = list(map(int, input().split()))
    num = arr[0]
    ave = average()
    print('{:.3f}%'.format(ratio()))