import sys
sys.stdin = open('input.txt')

dic = {}

while True:
    try: 
        line = input()
        for chr in line:
            dic.setdefault(chr, 0)
            dic[chr] += 1
    except:
        break

if ' ' in dic:
    del dic[' ']

s = ''
for key in dic:
    if dic[key] == max(dic.values()):
        s += key

print(''.join(sorted(s)))