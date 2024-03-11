import sys
input = sys.stdin.readline

n = int(input())
ans = []


for _ in range(n):
    age,name = map(str, input().split())
    ans.append([int(age),name])
    
a = sorted(ans,key=lambda x: x[0])
for _ in range(n):
    print(*a[_])