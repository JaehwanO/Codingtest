from collections import deque

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []
def bfs(graph,a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    area = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = 0 
                q.append((nx,ny))
                area += 1

    return area 

c = 0 
ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tmp = bfs(graph,i,j)
            c += 1
            ans = max(ans,tmp)
print(c)
print(ans)
# if not ans:
#     print(0)
# else:
#     print(max(ans))