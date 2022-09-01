from collections import deque
stop = 1

def bfs(a,b):
    dx = [1,-1,0,0,1,-1,-1,1]
    dy = [0,0,1,-1,1,-1,1,-1]
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            #여기가 중요
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])

while True: 
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    graph = []
    cnt = 0
    for _ in range(m):
        graph.append(list(map(int, input().split())))
    # print(graph)
    # print(n,m)

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt+=1
    print(cnt)