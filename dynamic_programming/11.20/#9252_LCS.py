import sys
input = sys.stdin.readline
a = [0] + list(input().strip())
b = [0] + list(input().strip())
len_a = len(a)
len_b = len(b)
dp = [[""] * len_b for i in range(len_a)]

for i in range(1, len_a):
    for j in range(1, len_b):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(len(dp[len_a - 1][len_b - 1]))
print(dp[len_a - 1][len_b - 1])


# s1 = [''] + list(map(str,input()))
# s2 = [''] + list(map(str,input()))

# dp = [[0]*len(s1) for _ in range(len(s2))]
# ans = ''
# for i in range(1,len(s2)):
#     for j in range(1,len(s1)):
#         if s2[i] != s1[j]:
#             dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
#         else:
#             dp[i][j] = dp[i-1][j-1] + 1

# m = max(dp[len(s2)-1])
# for i in range(len(s2)-1,0,-1):
#     for j in range(len(s1)):
#         if dp[i][j] == m:
#             m -= 1
#             ans += s1[j]
#             break
#         if m == 0:
#             break

# if dp[len(s2)-1][len(s1)-1] != 0:
#     print((dp[len(s2)-1][len(s1)-1]))
#     print(ans[::-1])
# else:
#     print(dp[len(s2)-1][len(s1)-1])