from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)

# from collections import deque

# def dfs(x,y):
#     if x <=-1 or x>=m or y<=-1 or y >=n:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         #모든곳을 방문하고 1로 만든다
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# T = int(input())
# for _ in range(T):
#     answer = []
#     result = 0
#     graph = []
#     m,n,k = map(int,input().split())
#     graph = [[0]*m for i in range (n)]
#     # print(k)
#     for i in range (k):
#         a,b = map(int, input().split())
#         graph[b][a] = 1
#     # print(graph)

#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j)==True:
#                 result +=1