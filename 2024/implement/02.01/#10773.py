import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    a = int(input())
    if s and a==0:
        s.pop()
    else:
        s.append(a)

print(sum(s))    