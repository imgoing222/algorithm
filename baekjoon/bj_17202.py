import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A = input()
B = input()
C = []
for i in range(8):
    C.append(int(A[i]))
    C.append(int(B[i]))

while len(C) > 2:
    for j in range(len(C) - 1):
        if C[j] + C[j+1] > 9:
            C[j] = C[j] + C[j+1] - 10
        else:
            C[j] = C[j] + C[j+1]
    C.pop()

print(''.join(map(str, C)))



