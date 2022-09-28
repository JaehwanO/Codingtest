
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)
# from collections import deque


# n, m = map(int,input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def find_min(graph):
#     mini = 10
#     for i in graph:
#         for j in i:
#             if int(j)!=0:
#                 mini=min(mini,int(j))
#     return mini

# def bfs(a,b):
#     visited = [[False]*m for i in range (n)]
#     mini = graph[a][b]
#     q = deque()
#     q.append((a,b))
#     visited[a][b] = True
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<m and int(graph[nx][ny])>=mini and int(graph[nx][ny])!=0 and visited[nx][ny]==False:
#                 visited[nx][ny]=True
#                 graph[nx][ny] = int(graph[nx][ny])-mini
#                 q.append((nx,ny))
#     graph[a][b] = 0



# def bfs_check(a,b,graph):
#     cnt = 0
#     visited = [[False]*m for i in range (n)]
#     q = deque()
#     q.append((a,b))
#     visited[a][b] = True
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<m and graph[nx][ny]>0 and visited[nx][ny]==False:
#                 visited[nx][ny]=True
#                 graph[nx][ny] = 0
#                 q.append((nx,ny))
            
# cnt = 0
# while cnt < 2:
#     for i in range(n):
#         for j in range(m):
#             if int(graph[i][j])==find_min(graph):
#                 bfs(i,j)
#                 break
  
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j]!=0:
#                 bfs_check(i,j,graph)
#                 cnt += 1
# print(cnt)