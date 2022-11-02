# 2800 괄호 제거
import itertools
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations

def find_pair():
    li = []
    for i in range(len(expression)):
        if expression[i] == '(' or expression[i] == ')':
            li.append(i)

    for i in range(len(li)//2):
        pair.append([li[i], li[len(li)-1-i]])


expression = input().rstrip()
pair = []
find_pair()

case = []
for i in range(1, len(pair)+1):
    case.extend(itertools.combinations(pair, i))

print(case)