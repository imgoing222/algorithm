for i in range(3):
    li = list(map(int, input().split()))
    zero = 0
    
    for j in range(len(li)):
        if li[j] == 0:
            zero += 1

    if zero == 1:
        print('A')
    elif zero == 2:
        print('B')
    elif zero == 3:
        print('C')
    elif zero == 4:
        print('D')
    else:
        print('E')
