n = int(input())
for i in range(n):
    a = int(input())
    for i in range(2, a + 1):
        count = 0
        if a % i == 0:
            while a % i == 0:
                a = a // i
                count += 1
            print('%d %d' %(i, count))
        elif a == 1:
            break
        
# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     d = {}
#     d[2] = 0
#     d[3] = 0
#     d[5] = 0
#     d[7] = 0
#     n = int(input())
#     while n !=1:
#         if n%2 == 0:
#             d[2] += 1
#             n = n //2
#         elif n%3 == 0:
#             d[3] += 1
#             n = n //3
#         elif n%5 == 0:
#             d[5] += 1
#             n = n //5
#         elif n%7 == 0:
#             d[7] += 1
#             n = n //7

#     for k, v in d.items():
#         if v != 0:
#             print(k,v)