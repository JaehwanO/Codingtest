n = int(input())
dp = [0] * 100001
square = [i * i for i in range(1, 317)]

for i in range(1,n+1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])