from collections import deque

n,m,k=map(int,input().split())

graph = [[0]*m for i in range(n)]

for _ in range(k):
    a,b,c,d, = map(int,input().split())
    for i in range(b,d):
        for j in range(a,c):
            graph[i][j]=1
answer=[]
def bfs(a,b):
    area = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append((a,b))
    graph[a][b]=1
    while q:
        x,y = q.popleft()
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=1
                q.append((nx,ny))
                area += 1
    answer.append(area)
cnt = 0 
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            cnt +=1
            bfs(i,j)
print(cnt)
answer.sort()
for i in answer:
    print(i,end=" ")
# print(answer)
