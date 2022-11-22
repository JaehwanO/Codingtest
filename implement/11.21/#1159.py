from collections import defaultdict
n = int(input())
d = defaultdict(int)

for _ in range(n):
    d[input()[0]] += 1

d = sorted(d.items())
s = ''

for k,v in d:
    if v >= 5:
        s += k

if s:
    print(s)
else:
    print("PREDAJA")

