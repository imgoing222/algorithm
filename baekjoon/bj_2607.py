# 2607 비슷한 단어
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def compare(a, b):
    global cnt

    length_b = len(b)

    if len(a) == length_b:
        if a == b:
            cnt += 1
            return
        else:
            if chk(a, b) == len(a) - 1:
                cnt += 1
                return

    else:
        if len(a) > length_b:
            if chk(a, b) == length_b:
                cnt += 1
                return
        else:
            if chk(a, b) == len(a):
                cnt += 1
                return

def chk(a, b):
    res = 0
    for letter in a:
        if letter in b:
            res += 1
            b.remove(letter)
    return res


N = int(input())
cnt = 0
word1 = sorted(list(input().rstrip()))

for _ in range(N-1):
    word2 = sorted(list(input().rstrip()))

    if abs(len(word1)-len(word2)) <= 1:
        compare(word1, word2)

print(cnt)