# 1464 뒤집기 3
import sys
sys.stdin = open('input.txt')

def change_pos(x):
    new_S = ''
    new_S += S[x]
    new_S += S[:x]
    new_S += S[x+1:]

    return new_S

S = input()

for i in range(len(S)-1):
    if S[i] > S[i+1] and S[i+1] <= S[0]:
        S = change_pos(i+1)

print(S)