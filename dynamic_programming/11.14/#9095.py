t = int(input())

dp = [0]*12
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = dp[3-1] + dp[3-2] + dp[3-3]

for i in range(3,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])