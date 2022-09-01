#dfs
n = int(input())
graph = []
answer = [] 

for _ in range (n):
    graph.append(list(map(int,input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    if x <=-1 or x>=n or y<=-1 or y >=n:
        return False
    if graph[x][y]==1:
        global area
        area += 1
        graph[x][y]=0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False
    
area = 0
result = 0 
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            answer.append(area)
            result += 1
            area = 0
print(result)
print(answer)


#bfs
# from collections import deque

# n = int(input())
# graph = []
# answer = []
# for _ in range (n):
#     graph.append(list(map(int,input())))

# def bfs(a,b):
#     area = 1
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     queue = deque()
#     queue.append((a,b))
#     graph[a][b] = 0
#     while queue:
#         x,y=queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             #여기가 중요
#             if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 area += 1
#                 queue.append([nx, ny])
#     answer.append(area)

# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if graph[i][j]==1:
#             bfs(i,j)
#             cnt +=1 
# print(cnt)
# if answer:
#     answer.sort()
#     for i in answer:
#         print(i)
# else:
#     print(0)