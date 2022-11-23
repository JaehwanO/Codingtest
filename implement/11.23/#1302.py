from collections import defaultdict

n = int(input())
d = defaultdict(int)

for _ in range(n):
    d[input()] += 1

ans = sorted(d.items(),key=lambda x : (-x[1],x[0]) )
print(ans[0][0])