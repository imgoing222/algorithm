A, B = input().split()

def find():
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a == b:
                x, y = i, j
                return x, y

position = find()
res = ''

for i in range(len(B)):
    s = ''
    for j in range(len(A)):
        if i == position[1]:
            s += A[j]
        elif j == position[0]:
            s += B[i]
        else:
            s += '.'
    res += (s + '\n')
    
print(res.rstrip())


