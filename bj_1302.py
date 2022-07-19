# 1302 베스트셀러
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
counting_books = defaultdict(int)

for _ in range(N):
    book = input().rstrip()
    counting_books[book] += 1

best_seller = [key for key, value in counting_books.items() if value == max(counting_books.values())]

print(sorted(best_seller)[0])


