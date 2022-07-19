import sys
sys.stdin = open('input.txt')
from itertools import permutations

N = int(input())

oAy, oAx = map(int, input().split())
oBy, oBx = map(int, input().split())
oCy, oCx = map(int, input().split())

Ay, Ax = oAy, oAx
By, Bx = oBy, oBx
Cy, Cx = oCy, oCx


case = [[oAy, oBx, 0], [oAy, oCx, 1], [oBy, oAx, 2], [oBy, oCx, 3], [oCy, oAx, 4], [oCy, oBx, 5]]

perm = list(permutations(case))

for i in perm:
    ans = []
    Ay, Ax = oAy, oAx
    By, Bx = oBy, oBx
    Cy, Cx = oCy, oCx

    for j in range(len(i)):
        if i[j][2] == 0:
            m = min(Ay, Bx)
            Ay -= m
            Bx -= m
        elif i[j][2] == 1:
            m = min(Ay, Cx)
            Ay -= m
            Cx -= m
        elif i[j][2] == 2:
            m = min(By, Ax)
            By -= m
            Ax -= m
        elif i[j][2] == 3:
            m = min(By, Cx)
            By -= m
            Cx -= m
        elif i[j][2] == 4:
            m = min(Cy, Ax)
            Cy -= m
            Ax -= m
        else:
            m = min(Cy, Bx)
            Cy -= m
            Bx -= m

        ans.append((i[j][2], m))

    if Ax + Ay + Bx + By + Cx + Cy == 0:
        print(1)
        ans.sort()
        for i in range(0, 6, 2):
            print(ans[i][1], ans[i+1][1])
        exit()

print(0)