import sys
input = sys.stdin.readline
 
n = int(input())
cnt = 0
 
for _ in range(n):
    s = input().rstrip()
    stack = []
 
    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
 
    if not stack:
        cnt += 1
print(cnt)

# n = int(input())
# ans = 0
# for _ in range(n):
#     s = input()
#     l = []
#     a_cnt = 0
#     b_cnt = 0
#     for i in s:
#         if a_cnt%2==0 and i == "A":
#             l.append(i)
#             a_cnt += 1
#         elif a_cnt%2==1 and i == "A" and l[-1]== "A":
#             l.pop()
#             a_cnt -=1

#         elif b_cnt%2==0 and i == "B":
#             l.append(i)
#             b_cnt += 1

#         elif b_cnt%2==1 and i == "B" and l[-1]== "B":
#             l.pop()
#             b_cnt -=1        
#     # print(l)
#     if not l:
#         ans+=1
# print(ans)