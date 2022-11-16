# n,c = map(int,input().split())

# w = list(map(int,input().split()))
# dp = [[1 for _ in range(c+1)] for _ in range(n)]
# w.sort()
# for i in range(c+1):
#     if i<w[0]:
#         dp[0][i] = 1
#     else:
#         dp[0][i] = 2

# for i in range(1,n):
#     for j in range(c+1):
#         if j<w[i]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+dp[i-1][j])

# print(dp[n-1][c])

# Meet In The Middle