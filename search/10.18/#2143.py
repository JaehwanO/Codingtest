##
import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

d = defaultdict(int)
ans = 0
for i in range(n):
    for j in range(i,n):
            d[sum(a[i:j+1])] += 1

for i in range(m):
    for j in range(i,m):
        ans += d[t - sum(b[i:j+1])]

print(ans)
