word = input()
i = 0
cnt = 0
try:
    while True:
        if word[i] == '':
            break
        else:
            cnt += 1
            i += 1
except:
    print(cnt)
