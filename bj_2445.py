N = int(input())

for i in range(1, 2*N):
    if i < N:
        star = '*'*i + ' '*(2*N-2*i) + '*'*i
        print(star)
    else:
        star = '*'*(2*N-i) + ' '*(2*N-2*(2*N-i)) + '*'*(2*N-i)
        print(star)