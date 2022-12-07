import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int,input().split()))
l.sort()
ans = 0
for i in range(n):
    for j in range(i,n):
        ans += l[j]-l[i]
print(ans*2)