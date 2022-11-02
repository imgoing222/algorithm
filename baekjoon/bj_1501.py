# 1501 영어 읽기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def case(word):
    cnt = 0
    middle = sorted(list(word[1:len(word)-1]))

    for d_word in dict:
        if len(d_word) == len(word):
            if d_word[0] == word[0] and d_word[-1] == word[-1]:
                d_middle = sorted(list(d_word[1:len(d_word)-1]))
                if d_middle == middle:
                    cnt += 1
    return cnt

N = int(input())
dict = [input().rstrip() for _ in range(N)]

M = int(input())
for _ in range(M):
    sentence = list(input().rstrip().split())
    ans = 1

    for word in sentence:
        ans *= case(word)

    print(ans)