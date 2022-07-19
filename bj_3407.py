# 3407 맹세
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

periodic_table = {
    'a': ['l', 'r', 'u', 'g', 't', 'm', 'c', 's'],
    'b': ['', 'e', 'r', 'a', 'i', 'h', 'k'],
    'c': ['', 'l', 'a', 'r', 'o', 'u', 'd', 's', 'n', 'e', 'm', 'f'],
    'd': ['b', 's'],
    'e': ['u', 'r', 's'],
    'f': ['', 'e', 'r', 'l', 'm'],
    'g': ['a', 'e', 'd'],
    'h': ['', 'e', 'f', 'g', 's', 'o'],
    'i': ['', 'n', 'r'],
    'k': ['', 'r'],
    'l': ['i', 'v', 'u', 'a', 'r'],
    'm': ['g', 'n', 'o', 't', 'd'],
    'n': ['', 'a', 'e', 'i', 'b', 'd', 'p', 'o'],
    'o': ['', 's'],
    'p': ['', 'd', 't', 'b', 'o', 'r', 'm', 'a', 'u'],
    'r': ['u', 'h', 'e', 'f', 'g', 'a'],
    's': ['', 'i', 'e', 'c', 'r', 'g', 'm'],
    't': ['i', 'c', 'e', 'l', 'b', 'm', 'h'],
    'u': [''],
    'v': [''],
    'w': [''],
    'x': ['e'],
    'y': ['b', ''],
    'z': ['n', 'r'],
}




T = int(input())
for _ in range(T):
    word = input()
    i = 1
    while i < len(word):
        dfs(word[i-1], word[i]) 