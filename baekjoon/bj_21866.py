scores = list(map(int, input().split()))

max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

if sum(scores) < 100:
    print('none')
else:
    for i in range(len(scores)):
        if max_score[i] < scores[i]:
            print('hacker')
            exit()
    print('draw')