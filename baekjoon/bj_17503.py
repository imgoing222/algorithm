import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M, K = map(int, input().split())
beers = []
alcohol_set = set()

for _ in range(K):
    v, c = map(int, input().split())
    alcohol_set.add(c)
    beers.append((v, c))

beers.sort(reverse=True)
alcohols = sorted(alcohol_set)

for liver in alcohol_set:
    i = num = likes = 0
    while True:
        if i >= len(beers):
            break

        if liver >= beers[i][1]:
            num += 1
            likes += beers[i][0]

        if num == N:
            if M <= likes:
                print(liver)
            else:
                break            
            exit()

        i += 1

print(-1)