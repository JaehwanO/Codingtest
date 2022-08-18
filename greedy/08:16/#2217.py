import sys

n = int(sys.stdin.readline())
l = []
m = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in l:
    m.append(i*n)
    # print(i*n)
    n-=1
print(max(m))