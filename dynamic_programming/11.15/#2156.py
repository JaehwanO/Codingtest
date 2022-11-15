n = int(input())
a = [int(input()) for _ in range(n)]

dp = [0] * (n+1)

dp[0] = a[0]
if n>1:
    dp[1] = dp[0] + a[1]
    if n>2:
        dp[2] = max(a[2]+a[0], a[2]+a[1], dp[1])
        for i in range(3,n):
            dp[i] = max(a[i]+dp[i-2],a[i]+a[i-1]+dp[i-3],dp[i-1])

print(max(dp))