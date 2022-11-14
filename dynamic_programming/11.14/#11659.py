import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = [0] + list(map(int,input().split()))
dp = [0] * (n+1)
dp[1] = num[1]
for i in range(2,n+1):
    dp[i] = num[i] + dp[i-1]

for _ in range (m):
    left ,right = map(int,input().split())
    print(dp[right] - dp[left-1])