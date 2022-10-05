import sys
n, m = map(int,sys.stdin.readline().split())
d = {}
for _ in range(n):
    a, b = map(str,sys.stdin.readline().split())
    d[a] = b

# print(d)
for _ in range(m):
    c = sys.stdin.readline().rstrip()
    print(d[c])