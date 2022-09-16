import sys
from collections import deque
# input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

def bfs(a,b,visited,graph):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append((a,b))
    visited[a][b]=True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and graph[nx][ny]==graph[x][y]:
                visited[nx][ny]=True
                q.append((nx,ny))


def three():
    visited = [[False]*n for i in range (n)]
    cnt = 0 
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='R' and visited[i][j]==False:
                bfs(i,j,visited,graph)
                cnt += 1
            if graph[i][j]=='G' and visited[i][j]==False:
                bfs(i,j,visited,graph)
                cnt += 1
            if graph[i][j]=='B' and visited[i][j]==False:
                bfs(i,j,visited,graph)
                cnt += 1
    return cnt

def two():
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='G':
                graph[i][j]='R'
    # print(graph)
    visited = [[False]*n for i in range (n)]
    cnt = 0 
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='R' and visited[i][j]==False:
                bfs(i,j,visited,graph)
                cnt += 1
            if graph[i][j]=='B' and visited[i][j]==False:
                bfs(i,j,visited,graph)
                cnt += 1
    # print(visited)
    return cnt

print(three(),two())