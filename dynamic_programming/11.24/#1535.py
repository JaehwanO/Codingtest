n = int(input())
tmp1 = list(map(int,input().split()))
tmp2 = list(map(int,input().split()))

wv = [[0,0]]
for i in range(n):
    wv.append((tmp1[i],tmp2[i]))

dp = [[0]*101 for _ in range(n+1)]

for i in range(1,n+1):
    w = wv[i][0]
    v = wv[i][1]
    for j in range(1,101):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v+dp[i-1][j-w],dp[i-1][j])
print(dp[n][99])
