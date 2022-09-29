n = int(input())
a = [int(input()) for _ in range(n)]

pos = []
neg = []

for i in a:
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)

pos.sort()
neg.sort(reverse=True)

ans = 0

while len(pos) >= 2:
    a = pos.pop()
    b = pos.pop()

    if a == 1 or b == 1:
        ans += a + b
    else:
        ans += a * b

if pos:
    ans += pos.pop()

while len(neg) >= 2:
    a = neg.pop()
    b = neg.pop()

    ans += a * b

if neg:
    ans += neg.pop()

print(ans)


# n = int(input())
# positive = []
# negative = []
# ans = []
# for _ in range(n):
#     s = int(input())
#     if s<=0:
#         negative.append(s)
#     else:
#         positive.append(s)
# # print(negative,positive)
# negative.sort(reverse=True)
# positive.sort()
# # print(negative,positive)
# while positive:
#     if len(positive)>1:
#         if positive[-1]*positive[-2]>1:
#             ans.append((positive.pop()*positive.pop()))
#         else:
#             ans.append(positive.pop()+positive.pop())
#     else:
#         ans.append(positive.pop())
        
# while negative:
#     if len(negative)>1:
#         ans.append((negative.pop()*negative.pop()))
#     else:
#         ans.append(negative.pop())

# print(sum(ans))
