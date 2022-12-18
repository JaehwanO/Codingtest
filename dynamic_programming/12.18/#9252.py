s1 = [0] + list(input())
s2 = [0] + list(input())
len1 = len(s1)
len2 = len(s2)

dp = [['']*len2 for _ in range(len1)]

for i in range(1,len1):
    for j in range(1,len2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
print(dp)