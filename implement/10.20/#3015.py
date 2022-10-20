import sys
input=sys.stdin.readline
s=[]
a=0

for _ in range(int(input())):
    m = int(input())
    while s and s[-1][0]<m:
        a+=s.pop()[1]

    if not s: 
        s.append((m,1))

    elif s[-1][0]==m:
        c=s.pop()[1]
        a+=c
        if s:
            a+=1
        s.append((m,c+1))

    else:
        s.append((m,1))
        a+=1
print(a)

# import sys
# input = sys.stdin.readline

# n = int(input())

# s = []

# for _ in range(n):
#     s.append(int(input()))
# # print(s)

# cnt = 0 
# for left in range(n):
#     right = left + 1
#     first = s[left]
#     tmp = [0]

#     while right < n:
#         if tmp[-1] <= first and tmp[-1] <= s[right]:
#             tmp.append(s[right])
#             right += 1
#             cnt += 1
#         else:
#             break
        
# print(cnt)