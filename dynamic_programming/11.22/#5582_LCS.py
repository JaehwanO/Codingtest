s1 = [0] + list(input())
s2 = [0] + list(input())

dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

# print(dp)
ans = 0
for i in range(1,len(s2)):
    for j in range(1,len(s1)):
        if s2[i] == s1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans,dp[i][j])
print(ans)