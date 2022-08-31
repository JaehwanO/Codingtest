from collections import deque
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []
def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    area = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                area +=1
    answer.append(area)
    return
cnt = 0
for a in range(n):
    for b in range(m):
        if graph[a][b] == 1:
            cnt += 1
            bfs(a,b)
print(cnt)
if not answer:
    print(0)
else:
    print(max(answer))