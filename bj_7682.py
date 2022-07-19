# 7682 틱택토
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    if input().rstrip() == 'end':
        break
    board = input().rstrip()
    
