n = int(input())
a = [0] + list(map(int,input().split()))

dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(1,i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))