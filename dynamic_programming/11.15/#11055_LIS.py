n = int(input())
a = [0] + list(map(int,input().split()))
dp = [0] * (n+1)

dp[1] = a[1]
# dp[2] = a[1] + a[2]
for i in range(2,n+1):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += a[i]

print(max(dp))