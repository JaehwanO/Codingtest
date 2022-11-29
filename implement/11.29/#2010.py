import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n-1):
    ans += int(input())-1
ans += int(input())
print(ans)