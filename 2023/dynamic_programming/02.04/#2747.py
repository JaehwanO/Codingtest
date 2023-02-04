dp = [0,0,0]
dp[0] = 0
dp[1] = 1
dp[2] = 1

n = int(input())
for i in range(2,n):
    dp.append(dp[-1]+dp[-2])
print(dp[n])