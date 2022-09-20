n = int(input())
l = []
dp = [0] * 10000
for _ in range(n):
    l.append(int(input()))

# print(l)
dp[0] = l[0]
dp[1] = l[0] + l[1]
dp[2] = max(l[1] + l[2], l[0] + l[2],l[0])

for i in range(3,n):
    dp[i] = max(dp[i-3] + l[i-1] + l[i], dp[i-2] + l[i], dp[i-1])
    #6 + 13 + 9, 16+9
    # print(dp)
print(max(dp))


# n = int(input())
# s = [0 for i in range(301)]
# dp = [0 for i in range(301)]
# for i in range(n):
#     s[i] = int(input())
# dp[0] = s[0]
# dp[1] = s[0] + s[1]
# dp[2] = max(s[1] + s[2], s[0] + s[2])
# for i in range(3, n):
#     dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
# print(dp[n - 1])