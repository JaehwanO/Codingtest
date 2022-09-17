import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range (n):
    graph.append(list(input().strip()))
# print(graph)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    maxi = 0
    q = deque()
    q.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]==False and graph[nx][ny] != "W":
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                maxi = max(maxi,graph[nx][ny])
                q.append([nx, ny])
    return maxi

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != "W":
            visited = [[False]*m for i in range (n)]
            graph[i][j]=0
            visited[i][i] = True
            result = max(result,bfs(i,j))
print(result)