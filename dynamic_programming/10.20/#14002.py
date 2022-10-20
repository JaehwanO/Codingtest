n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i],dp[j] + 1)

print(max(dp))
order = max(dp)
sub = []
for i in range(n-1,-1,-1):
    if dp[i] == order:
        sub.append(a[i])
        order -= 1
sub.reverse()
print(*sub)