n = int(input())
dp = [0,1]

for i in range(1,n):
    dp.append(dp[i]+dp[i-1])
print(dp[n])