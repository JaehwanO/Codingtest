from collections import defaultdict
# import sys

# input = sys.stdin.readline
n,m = map(int,input().split())
d = defaultdict(int)

for _ in range(n):
    d[input()] += 1
for _ in range(m):
    d[input()] += 1

# print(list(d.values()))
cnt = list(d.values()).count(2)
d = sorted(d.items(), key = lambda x : (x[1],x[0]))
print(cnt)
for k,v in d:
    if v == 2:
        print(k)