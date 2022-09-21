n, k = map(int,input().split())
s = []
for _ in range(n):
    s.append(int(input()))
s.sort()
dp = [0] *(k+1)
dp[0] = 1
for i in s:
    for j in range(i,k+1):
        dp[j] += dp[j-i]
    # print(dp)
print(dp[k])


#     1 2 3 4 5 6 7 8 9 10
# 1   1 1 1 1 1 1 1 1 1 1
# 2   0 1 1 2 2 3 3 4 4 5 
# 5   0 0 0 0 1 1 2 2 3 4
# t   1 2 2 3 4 5 5 7 8 10  