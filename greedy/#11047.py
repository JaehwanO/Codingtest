N, K = map(int, input().split()) 
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//coin_lst[i] 
    K = K%coin_lst[i] 

print(count)

# n, k = map(int, input().split())
# l = []
# for _ in range(n):
#     l.append(int(input()))
# # print(l)
# cnt = 0
# while  k !=0:
#     for i in l:
#         if len(str(i)) == len(str(k)) and i<=k:
#             # print(i)
#             cnt+=1
#             k -=i
#             # print(len(str(k)))
#         else:
#             pass
# print(cnt)