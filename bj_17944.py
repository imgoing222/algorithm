n, T = map(int, input().split())

li = [i for i in range(1, 2*n + 1)] + [i for i in range(2*n - 1, 1, -1)]

print(li[(T - 1) % len(li)])