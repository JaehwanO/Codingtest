dp = [[1] * 31 for _ in range(31)]
for i in range(31):
    dp[1][i] = i
for i in range(2, 31):
    for j in range(i + 1, 31):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])