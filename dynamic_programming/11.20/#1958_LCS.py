import sys
input = sys.stdin.readline
a = [0] + list(input().strip())
b = [0] + list(input().strip())
c = [0] + list(input().strip())
len_a = len(a)
len_b = len(b)
len_c = len(c)
dp = [[[0 for _ in range(len_c)] for _ in range(len_b)] for _ in range(len_a)]

# print(dp[0])
for i in range(1, len_a):
    for j in range(1, len_b):
        for k in range(1,len_c):
            if a[i] == b[j] and b[j] == c[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
print(dp[len_a - 1][len_b - 1][len_c-1])

