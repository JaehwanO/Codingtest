# from collections import defaultdict 
# n,m = map(int,input().split())

# d = defaultdict(set)
# for i in range(n+1):
#     d[i].add(i)

# for _ in range(m):
#     oper, a, b = map(int,input().split())
#     tmp_set = {a,b}
#     if oper == 0:
#         d[a] = d[a].union(d[b])
#         d[b] = d[a]
#     if oper == 1:
#         if d[a].intersection(tmp_set) == tmp_set or d[b].intersection(tmp_set) == tmp_set:
#             print("Yes")
#         else:
#             print("NO")

# union find