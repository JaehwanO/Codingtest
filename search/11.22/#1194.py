from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    while q:
        if q:
            x,y,c,cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != "#" and visited[nx][ny][c] == 0:
                if graph[nx][ny] == '.':
                    visited[nx][ny][c] = 1
                    q.append([nx,ny,c,cnt+1])

                elif graph[nx][ny] == '1':
                    return cnt + 1

                elif graph[nx][ny].isupper():
                    if c & 1<<ord(graph[nx][ny])-65:
                        visited[nx][ny][c] = 1
                        q.append([nx,ny,c,cnt + 1])
                elif graph[nx][ny].islower():
                    nc = c | 1<<ord(graph[nx][ny])-97
                    if visited[nx][ny][nc] == 0:
                        visited[nx][ny][nc] = 1
                        q.append([nx,ny,nc,cnt+1])
    return -1 

n, m = map(int,input().split())
graph = []
q = deque()
visited = [[[0]*64 for _ in range(m)]for _ in range(n)]
for i in range(n):
    tmp = list(map(str,input()))
    graph.append(tmp)
    for j in range (m):
        if tmp[j] == '0':
            q.append([i,j,0,0])
            graph[i][j] = '.'
            visited[i][j][0] = 1
print(bfs())
# print(ord("A"))
# print(ord("a"))