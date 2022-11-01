# from collections import Counter
# def rc():
#     max_len = 0
#     len_s = len(s)
#     for j in range(len_s):
#         a = [i for i in s[j] if i != 0]
#         a = Counter(a).most_common()
#         a.sort(key = lambda x : (x[1], x[0]))
#         s[j] = []
#         for fi, se in a:
#             s[j].append(fi)
#             s[j].append(se)
#         len_a = len(a)
#         if max_len < len_a * 2: 
#             max_len = len_a * 2
#     for j in range(len_s):
#         for k in range(max_len - len(s[j])):
#             s[j].append(0)
#         s[j] = s[j][:100]


# r, c, k = map(int, input().split())
# s = [list(map(int, input().split())) for i in range(3)]

# for i in range(101):
#     try:
#         if s[r - 1][c - 1] == k:
#             print(i)
#             break
#     except: 
#         pass
#     if len(s) < len(s[0]):
#         s = list(zip(*s))
#         rc()
#         s = list(zip(*s))
#     else:
#         rc()
# else:
#     print(-1)

# from collections import defaultdict, Counter

# r,c,k = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(3)]

# def R(arr):
#     tmp_m = 0
#     new_arr = [[] for _ in range(len(arr))]
#     for i in range(len(arr)):
#         tmp_set = set(arr[i])
#         tmp_arr = []
#         for j in tmp_set:
#             tmp_arr.append((j,arr[i].count(j)))
#         tmp_arr = sorted(tmp_arr, key = lambda x :(x[1],x[0]))
        
#         tmp_m = max(tmp_m,len(tmp_arr))
#         for k in tmp_arr:
#             for z in k:
#                 new_arr[i].append(z)
        
#     # print(tmp_m)
#     tmp_m *= 2
#     for p in range(len(new_arr)):
#         if len(new_arr[p]) < tmp_m:
#             # print("SMALAL")
#             for _ in range(tmp_m - len(new_arr[p])):
#                 new_arr[p].append(0)
#     # print(new_arr)
#     return new_arr

# a = R(arr)

# def C(arr):
#     col_arr = [[] for _ in range(len(arr[0]))]
#     for i in range(len(col_arr)):
#         for j in range(len(arr)):
#             col_arr[i].append(arr[j][i])
#     print(col_arr)

#     tmp_m = 0
#     new_arr = [[] for _ in range(len(col_arr))]
#     for i in range(len(col_arr)):
#         tmp_set = set(col_arr[i])
#         tmp_arr = []
#         for j in tmp_set:
#             tmp_arr.append((j,col_arr[i].count(j)))
#         tmp_arr = sorted(tmp_arr, key = lambda x :(x[1],x[0]))
#         print(tmp_arr)
#         tmp_m = max(tmp_m,len(tmp_arr))
 
        
#     # # print(tmp_m)
#     # tmp_m *= 2
#     # for p in range(len(new_arr)):
#     #     if len(new_arr[p]) < tmp_m:
#     #         # print("SMALAL")
#     #         for _ in range(tmp_m - len(new_arr[p])):
#     #             new_arr[p].append(0)
#     # print(new_arr)
#     # # return new_arr

# C(a)