import heapq
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = [(-graph[0][0],0,0)]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while q:
        h,x,y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]<graph[x][y]:
                if visited[nx][ny] == 0:
                    heapq.heappush(q,(-graph[nx][ny],nx,ny))
                visited[nx][ny] += visited[x][y]
    return visited[n-1][m-1]

print(bfs())