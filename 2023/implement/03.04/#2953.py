dp = [0]*5
for i in range(5):
    num = list(map(int,input().split()))
    s = sum(num)
    dp[i] = s

for i,num in enumerate(dp):
    if num == max(dp):
        print(i+1,num)
# # print(dp)