N = int(input())

# 양수, 음수, 1을 분리
positive=[]
negative=[]
one=[]

for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num <= 0:
        negative.append(num)
    else:
        one.append(num)

# 그리디 탐색에 맞게 양수는 내림차순, 음수는 오름차순으로 정렬
positive.sort(reverse=True)
negative.sort()

# 결과
result = 0

# 양수 리스트 입력
# 짝수일때
if len(positive) % 2 == 0:
    for i in range(0,len(positive),2):
        result += positive[i] * positive[i+1]
# 홀수일때
else:
    for i in range(0,len(positive)-1,2):
        result += positive[i] * positive[i+1]
    result += positive[len(positive)-1]

# 음수 리스트 입력
# 짝수일때
if len(negative) % 2 == 0:
    for i in range(0,len(negative),2):
        result += negative[i] * negative[i+1]
# 홀수일때
else:
    for i in range(0,len(negative)-1,2):
        result += negative[i] * negative[i+1]
    result += negative[len(negative)-1]

result += sum(one)

print(result)

# from collections import deque
# n = int(input())
# l = []
# p = deque()
# m = deque()
# s = 0
# o = []

# for _ in range(n):
#     l.append(int(input()))
# l.sort()

# for i in range(n):
#     if l[i] < 0:
#         m.append(l[i])
#     elif l[i] == 0:
#         pass
#     elif l[i] == 1:
#         o.append(l[i])
#     else:
#         p.append(l[i])

# while m:
#     if len(m)%2 == 0:
#         s += m.popleft() *m.popleft()
#     else:
#         s += m.pop()
# while p:
#     if len(p)%2 == 0:
#         s += p.pop() * p.pop()
#         # s += p.pop() *p.pop()
#     else:
#         s += p.popleft()
#     # print(s)
# print(s+sum(o))