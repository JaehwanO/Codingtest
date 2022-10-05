import sys

n, m = map(int, sys.stdin.readline().split())

d = {}
for i in range (m):
    a = sys.stdin.readline().rstrip()
    d[a] = i

# print(d.items())
d = sorted(d.items(),key = (lambda x:x[1]))

cnt = 0
for i in d:
    if cnt == n:
        break
    print(i[0])
    cnt += 1