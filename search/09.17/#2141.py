# import sys
# input = sys.stdin.readline
# n = int(input())
# l = []
# d = [0]*(n)
# for _ in range(n):
#     l.append(list(map(int,input().split())))

# for i in range(1,n+1):
#         for j in range(n):
#             if l[j][0] == i:
#                 d[i-1] += (l[j][0]*l[j][1])%173920
#             else:
#                 d[i-1] += (abs((l[j][0]-i))*(l[j][0]*l[j][1]))%173920
# index = d.index(min(d))
# print(index+1)

n = int(input())
info = []
people = 0 
for i in range(n):
    x = list(map(int,input().split()))
    info.append(x)
    people+=x[1]

info = sorted(info)

mid = people//2

if (people%2)==1:
    mid+=1
count =0
for l,p in info:
    count += p 
    if count >=mid:
        print(l)
        break