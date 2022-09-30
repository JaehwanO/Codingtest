import sys
input = sys.stdin.readline
n = int(input())
l = [] 
for _ in range(n):
    l.append(list(map(int,input().split())))
l = sorted(l, key = lambda x: (x[1],x[0]))
for i in l:
    print(i[0], i[1])