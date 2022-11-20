s1 = [0] + list(input())
s2 = [0] + list(input())
len_s1 = len(s1)
len_s2 = len(s2)

dp = [['']*len_s1 for _ in range(len_s2)]

for i in range(1,len_s2):
    for j in range(1,len_s1):
        if s1[i] == s2[j]:
            dp[i][j] += dp[i-1][j-1] + s1[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(dp)
