n = int(input())
l = list(list(map(int,input().split())) for _ in range(n))
l = sorted(l, key = lambda x: x[0])

dp = [0] * n
for i in range(n):
    for j in range(i):
        if l[i][1] > l[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] +=1
print(n-max(dp))