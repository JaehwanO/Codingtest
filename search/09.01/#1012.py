dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    if x <=-1 or x>=n or y<=-1 or y >=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False
# def bfs(graph, a, b):
#     queue = deque()
#     queue.append((a,b))
#     graph[a][b] = 0

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx < 0 or nx >=n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))
#     return


t = int(input())
for _ in range(t):
    cnt = 0
    n,m,k=map(int,input().split())
    graph = [[0]*m for i in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        graph[a][b] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                cnt += 1
    print(cnt)