n,k = map(int,input().split())
wv = [[0,0]]+ list(list(map(int,input().split())) for _ in range(n))
dp = [[0]*(k+1) for _ in range(n+1)]
wv = sorted(wv,key = lambda x : x[0])
for i in range(1,n+1):
    for j in range(1,k+1):
        w = wv[i][0]
        v = wv[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[n][k])
