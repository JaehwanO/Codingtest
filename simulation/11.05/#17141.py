from collections import deque
from itertools import combinations

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(v):
    q = deque(v)
    visited = [[-1 for _ in range(n)]  for _ in range(n)]
    m = 0
    for x,y in q:
        visited[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != 1 and visited[nx][ny] == -1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
                    m = max(m,visited[x][y] + 1)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] != 1:
                return float('inf')
    return m

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range (n)]
virus = []
ans = float('inf')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i,j])

for v in combinations(virus,m):
    ans = min(bfs(v),ans)

if ans == float('inf'):
    print(-1)
else:
    print(ans)