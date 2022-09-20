n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
# print(l)

dp = [[0]*(i+1) for i in range(n)]

dp[0][0] = l[0][0]
if n > 1:
    dp[1][0] = dp[0][0]+l[1][0]
    dp[1][1] = dp[0][0]+l[1][1]

for i in range(2,n):
    for j in range(len(l[i])):
        if j == 0 :
            dp[i][j] = l[i][j] + dp[i-1][0]
        elif j == len(l[i])-1:
            dp[i][j] = l[i][j] + dp[i-1][j-1]
        else:
            dp[i][j]=max(l[i][j]+dp[i-1][j-1], l[i][j]+dp[i-1][j])

print(max(dp[n-1]))