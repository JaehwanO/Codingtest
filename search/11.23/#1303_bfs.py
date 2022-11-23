from collections import deque

m,n = map(int,input().split())
graph = list(list(input()) for _ in range(n))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b,s,visited):
    cnt = 1
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==s and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    return cnt**2

visited = [[False]*m for _ in range(n)] 
white = 0
black = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs(i,j,'W',visited)
        elif graph[i][j] == 'B' and not visited[i][j]:
            black += bfs(i,j,'B',visited)

print(white,black)
