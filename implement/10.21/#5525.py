N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)

# import sys
# input = sys.stdin.readline

# n = int(input())
# tmp = 'OI'

# if n  <= 1:
#     p = 'IOI'
# else:
#     p = 'IOI' + tmp*(n-1)

# p = list(p)
# m = int(input())
# s = list(input())
# cnt = 0

# for i in range(m-len(p)):
#     # print(s[i:i+len(p)])
#     if s[i:i+len(p)] == p:
#         cnt += 1
# print(cnt)