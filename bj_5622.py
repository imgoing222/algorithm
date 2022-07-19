s = input()
time = 0

tel = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

for i in range(len(s)):
    for j in range(len(tel)):
        for k in range(len(tel[j])):
            if s[i] == tel[j][k]:
                time += (2 + j)

print(time)