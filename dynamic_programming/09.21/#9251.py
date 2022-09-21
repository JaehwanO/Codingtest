w1=list(input())
w2=list(input())
# print(w1,w2)
dp = [0] * (len(w1)+1)
for i in range(len(w1)):
    cnt = 0
    for j in range(len(w2)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif w1[i] == w2[j]:
            dp[j] = cnt+1
print(max(dp))