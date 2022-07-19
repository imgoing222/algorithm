import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x_list = []
y_list = []

for line in sys.stdin:
    a = list(map(int, line.split()))
    x_list.append(a[0])
    y_list.append(a[1])

for i in x_list:
    if x_list.count(i) == 1:
        res_x = i

for j in y_list:
    if y_list.count(j) == 1:
        res_y = j

print(f'{res_x} {res_y}')
    

