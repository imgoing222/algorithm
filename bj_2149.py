import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

key = list(input().rstrip())
s = input()
length = len(s) // len(key)
code = list(map(list, zip(*[iter(s)]*length)))

r_code = list(map(list, zip(*code)))

order = []
for k in key:
    for i in range(len(key)):
        if k == sorted(key)[i]:
            if i not in order:
                order.append(i)
                break

for r in r_code:
    for j in order:
        print(r[j], end='')