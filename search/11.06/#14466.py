from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if (nx,ny) in road[x][y]:
                continue
            q.append((nx,ny))
            visited[nx][ny] = True

n,k,r = map(int,input().split())
road = [[[] for _ in range(n)]for _ in range(n)]
cnt = 0

for _ in range(r):
    sx,sy,ex,ey = map(int,input().split())
    road[sx-1][sy-1].append((ex-1,ey-1))
    road[ex-1][ey-1].append((sx-1,sy-1))

cows = []
for _ in range(k):
    x,y = map(int,input().split())
    cows.append((x-1,y-1))

for i , cow in enumerate(cows):
    visited = [[False]*n for _ in range(n)]
    bfs(cow[0],cow[1])
    for x,y in cows[i+1:]:
        if not visited[x][y]:
            cnt += 1
print(cnt)