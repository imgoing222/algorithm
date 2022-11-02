# 4900 7 더하기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

digits = ['063', '010', '093', '079', '106', '103', '119', '011', '127', '107']

def change_to_number(x):
    res = ''
    for i in range(len(x)//3):
        res += str(digits.index(x[i*3: i*3+3]))

    return res

def change_to_segment(x):
    res = ''
    for i in x:
        res += digits[int(i)]

    return res

while True:
    expression = input().rstrip()
    if expression == 'BYE':
        break

    n = expression.find('+')
    a = expression[:n]
    b = expression[n+1:len(expression)-1]

    num_a = int(change_to_number(a))
    num_b = int(change_to_number(b))

    num_c = num_a + num_b
    c = change_to_segment(str(num_c))

    print(f'{expression}{c}')

    