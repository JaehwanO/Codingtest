n = int(input())
house = list(list(map(int,input().split())) for _ in range(n))
dp = [[0,0,0] for _ in range(n)]
# print(dp)
dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]

for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = house[i][j] + min(dp[i-1][1], dp[i-1][2])
        if j == 1:
            dp[i][j] = house[i][j] + min(dp[i-1][0], dp[i-1][2])
        if j == 2:
            dp[i][j] = house[i][j] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))