# 다시


import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = []
answer = []
for i in range(n):
    while stack :
        if lst[stack[-1]] >= lst[i]:
            break
        else:
            stack.pop()
    if stack:
        answer.append(stack[-1] + 1)
    else :
        answer.append(0)
    stack.append(i)
print(' '.join(list(map(str, answer))))
 