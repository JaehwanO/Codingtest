from itertools import permutations

s = input()
d = {}
for i in range(len(s)):
    for j in range(len(s)):
        d[s[j:j+i+1]] = 1
        # print(s[j:j+i+1])
print(len(d))
