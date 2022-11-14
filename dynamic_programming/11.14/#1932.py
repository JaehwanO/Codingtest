n = int(input())
l = list(list(map(int,input().split())) for _ in range(n))

# print(l)
dp = [[0]*i for i in range(1,n+1)]
# print(dp)
dp[0][0] = l[0][0]

for i in range (1,n):
    length = len(dp[i])
    for j in range(length):
        if j == 0:
            dp[i][0] = dp[i-1][0] + l[i][0]
        elif j == length - 1:
            dp[i][length-1] = dp[i-1][length-2] + l[i][length-1]
        else:
            dp[i][j] = max(dp[i-1][j-1] + l[i][j],dp[i-1][j]+l[i][j])
print(max(dp[n-1]))

