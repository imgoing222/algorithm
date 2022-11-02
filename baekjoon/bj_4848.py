# 4848 집합 숫자 표기법
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find_number(x):
    cnt = 0
    for letter in x[::-1]:
        if letter == '{':
            return cnt - 1
        cnt += 1

numbers = ['']*16
for i in range(16):
    numbers[i] += '{'
    for j in range(i):
        numbers[i] += numbers[j] + ','
    numbers[i] = numbers[i].rstrip(',')
    numbers[i] += '}'
    
for _ in range(int(input())):
    a = input().rstrip()
    b = input().rstrip()
    
    num1 = find_number(a)
    num2 = find_number(b)

    print(numbers[num1+num2])

    