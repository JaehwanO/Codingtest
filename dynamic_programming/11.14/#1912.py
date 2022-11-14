n = int(input())
dp = [-1000] * (n+1)
l = [0] + list(map(int,input().split()))
dp[1] = l[1]

for i in range(1,n):
    dp[i+1] = max(l[i+1], dp[i] + l[i+1])

print(max(dp))