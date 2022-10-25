from itertools import combinations

n,m = map(int,input().split())
board= [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))
            
minv = float('inf')
for ch in combinations(chicken,m):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0]) + abs(home[1]-i[1]) for i in ch])
        if minv <= sumv:
            break
    if sumv < minv:
        minv = sumv
print(minv)

# import sys
# from collections import Counter, deque

# input = sys.stdin.readline

# n, m = map(int,input().split())
# l = []
# for _ in range(n):
#     l.append(list(map(int,input().rstrip().split())))
# # print(l)

# cnt = 0
# for i in l: 
#     cnt += i.count(2)
# # print(cnt)

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# ans = []
# def bfs(my_list):
#     global ans
#     for house in my_list:
#         mini = sys.maxsize
#         visited = [[False]*n for i in range(n)]
#         # print(chi)
#         q = deque()
#         a,b = house[0], house[1]
#         q.append((a,b))
#         visited[a][b] = True
#         print(q)
#         while q:
#             x,y = q.popleft()
#             # print(x,y)
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 # print(nx,ny)
#                 if 0<=ny<n and 0<=nx<n and visited[nx][ny]==False:
#                     if l[nx][ny] == 0:
#                         visited[nx][ny] = True
#                         q.append((nx,ny))
#                     if l[nx][ny] == 2:
#                         mini = min(mini,abs(nx-a) + abs(ny-b))
#                         # print(abs(nx-a) + abs(ny-b)
#                         continue
#         ans.append(mini)
#         # print(mini)

# bbq = []    
# for i in range(n):
#     for j in range(n):
#         if l[i][j] == 1:
#             bbq.append([i,j])

# bfs(bbq)
# ans.sort()
# print(sum(ans))