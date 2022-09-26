import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)



# import sys
# input = sys.stdin.readline

# n = int(input())
# l = list(map(int,input().split()))
# ans = []
# s = []

# for i in range(n):
#     k = i
#     while s:

#         if k >= n:
#             ans.append(-1)
#             break
#         if s[-1] < l[k]:
#             ans.append(l[k])
#             break
#         else:
#             k+=1

#     if i == n-1:
#         ans.append(-1)
#     s.append(l[i])
# print(' '.join(map(str,ans)))
# # print(ans)