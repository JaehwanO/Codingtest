
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    
print(max(dp))

# from bisect import bisect_left
# n = int(input())
# a = list(map(int,input().split()))
# tmp = [a[0]]
# for i in a:
#     x = bisect_left(tmp,i)
#     if x == len(tmp):
#         tmp.append(i)
#     elif tmp[x] > i:
#         tmp[x] = i

# print(len(tmp))
