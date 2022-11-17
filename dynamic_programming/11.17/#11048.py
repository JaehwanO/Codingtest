n,m = map(int,input().split())
a = list(list(map(int,input().split())) for _ in range(n))
dp = [[0]*m for _ in range(n)]
dp[0][0] = a[0][0]
for i in range(1,m):
    dp[0][i] = dp[0][i-1]+a[0][i]
for i in range(1,n):
    for j in range(m):
        if j == 0:
            dp[i][j] = dp[i-1][j] + a[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + a[i][j],dp[i-1][j-1] + a[i][j],dp[i][j-1] + a[i][j] )
print(dp[n-1][m-1])