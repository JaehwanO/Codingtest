from collections import deque

n = int(input())
graph = []
# dx  = [graph[0][0],0]
# dy  = [0,graph[0][0]]
for i in range(n):
    graph.append(list(map(int,input().split())))

visited = [[0]* n for _ in range(n)]

dx  = [1,0]
dy  = [0,1]
queue = deque()
queue.append((0,0))
while queue:
    x,y = queue.popleft()

    if graph[x][y]== -1:
        print("HaruHaru")
        exit(0)
    jump = graph[x][y]

    for i in range(2):
        nx = x + dx[i]*jump
        ny = y + dy[i]*jump
        
        if nx < 0 or nx>=n or ny <0 or ny>=n:
            continue
        elif 0 <= nx <n and 0<=ny<n and visited[nx][ny]==0:
            visited[nx][ny] =1
            queue.append([nx,ny])

print("Hing")

# print(graph)
