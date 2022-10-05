import sys
from collections import Counter
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = {}
    for _ in range (n):
        a,b = map(str,input().split())
        s[a] = b
    
    d = Counter(s.values())
    
    cnt = 1
    for key in d:
        cnt *= d[key] + 1
    print(cnt -1)


# t = int(input())

# for i in range(t):
#     n = int(input())
#     weardict = {}
#     for j in range(n):
#         wear = list(input().split())
#         if wear[1] in weardict:
#             weardict[wear[1]].append(wear[0])
#         else:
#             weardict[wear[1]] = [wear[0]]

#     cnt = 1 
#     for k in weardict:
#         cnt *= (len(weardict[k])+1)
#     print(cnt-1)
