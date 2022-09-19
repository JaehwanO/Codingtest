# 1 00

# 1 1 -> 1
# 2 11 00 -> 2
# 3 111 001 100  -> 3
# 4 0011 0000 1001 1100 1111 -> 5
n = int(input())
dp =[0,1,2]

for i in range(3,n+1):
    dp.append(dp[i-2]+dp[i-1])
print(dp[n])