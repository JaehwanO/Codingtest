import sys
input = sys.stdin.readline

n = int(input())
l = [0] + list(map(int,input().split()))
idx = [0] * (n+1)
for i in range(1,n+1):
    idx[l[i]] = i
cnt = 1
max = -1

for i in range(1,n):
    if idx[i] < idx[i+1]:
        cnt += 1
        if cnt > max:
            max = cnt
    else:
        cnt = 1

print(n-max)