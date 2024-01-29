import sys

d = {}
n,m = map(int, sys.stdin.readline().split())

for _ in range(n):
    a,b = map(str, sys.stdin.readline().split())
    d[a] = b

for _ in range(m):
    c = sys.stdin.readline().rstrip()
    print(d[c])