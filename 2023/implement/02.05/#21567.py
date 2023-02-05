ans = 1
for _ in range(3):
    ans *= int(input())

dp = [0]*10
for num in str(ans):
    dp[int(num)] += 1

for i in dp:
    print(i)