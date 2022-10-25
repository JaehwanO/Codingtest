import sys
N = int(sys.stdin.readline())
dp = [0]*1001
dp[1] = 1
# dp[2] = 0
dp[3] = 1
dp[4] = 1
# dp[5] = 1
for i in range(5, N+1):
    if not dp[i-1]:
        dp[i] = 1
    if not dp[i-3]:
        dp[i] = 1
    if not dp[i-4]:
        dp[i] = 1

# print(dp)
print('CY' if dp[N] == 0 else 'SK')