n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))


# from itertools import permutations
# num = list(input())
# per = permutations(num,len(num))
# m = 0 
# for i in per:
#     s = int(''.join(i))
#     # print(s)
#     if s%30 == 0:
#         m = max (m,s)
# if m == 0:
#     print(-1)
# else:
#     print(m)
