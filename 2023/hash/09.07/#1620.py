import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for i in range(n):
    name = input().rstrip()
    d[name] = i + 1
    d[i+1] = name


for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(d[int(a)])
    else:
        print(d[a])