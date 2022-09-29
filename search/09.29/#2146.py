import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
# print(graph)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def num_island(graph):
    num = 1
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                num+=1
                q.append((i,j))
                graph[i][j] = num
                while q:
                    x,y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                            graph[nx][ny] = num
                            q.append((nx,ny))
    return num

def bfs(is_num):
    visited = [[False]*n for i in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j]==is_num:
                q.append((i,j,0))
                visited[i][j]=True

    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<ny<n:

                if graph[nx][ny]!=0 and graph[nx][ny]!=is_num:
                    return dist
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny,dist+1))

ans = 300
for i in range(2,num_island(graph)):
    # print(bfs(i))
    ans = min(bfs(i),ans)
print(ans)
