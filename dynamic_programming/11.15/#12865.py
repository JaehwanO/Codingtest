n, k = map(int,input().split())
l = [[0,0]]
for _ in range(n):
    l.append(list(map(int,input().split())))
dp =[[0 for _ in range (k+1)] for _ in range(n+1)]
# for i in range(1,k+1):
#     dp[0][i] = 1



for i in range(1,n+1):
    for j in range(1,k+1):
        if j < l[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(l[i][1]+dp[i-1][j-l[i][0]], dp[i-1][j])
print(dp[n][k])