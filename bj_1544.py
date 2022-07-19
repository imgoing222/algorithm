# 1544 사이클 단어
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def chk():
    for i in ans:
            if len(i) == len(word):
                for j in range(len(i)):
                    if word[0] == i[j]:
                        new_word = ''
                        for k in range(len(i)):
                            new_word += i[(j+k)%len(i)]
                        if new_word == word:
                            return 1

N = int(input())
ans = []

for _ in range(N):
    word = input().rstrip()

    if not chk():
        ans.append(word)

print(len(ans))