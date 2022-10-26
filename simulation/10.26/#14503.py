import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r,c,d = map(int,input().split())

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 왼쪽으로 돈 방향
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]


# import sys
# from collections import deque
# input = sys.stdin.readline
# n, m = map(int,input().split())
# r,c,d = map(int,input().split())
# visited = [[False]*m for i in range (n)]
# graph = []

# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# heading = d
# clean = 1

# def bfs(a,b,heading):
#     global clean
#     q = deque()
#     q.append((a,b))
#     visited[a][b] = True
#     heading_count = 0

#     while q:
#         x,y = q.popleft()
        
#         #현재 방향의 왼쪽 방향
#         if heading == 0:
#             nx = x 
#             ny = y - 1
#         elif heading == 1:
#             nx = x - 1
#             ny = y 
#         elif heading == 2:
#             nx = x 
#             ny = y + 1
#         elif heading == 3:
#             nx = x + 1
#             ny = y 

#         if 0<=nx<n and 0<=ny<n:
#             # 청소가 된 곳
#             if visited[nx][ny]==True:
#                 #왼쪽으로 방향틀어서 탐색
#                 heading = (heading+3)%4
#                 # 청소가 되어있어 탐색한 횟수에 1 추가
#                 heading_count += 1
#                 q.append((x,y))
            
#             # 방문하지 않은곳
#             if visited[nx][ny] == False:
#                 # 벽
#                 if graph[nx][ny] == 1:
#                     #왼쪽으로 방향틀어서 탐색
#                     heading = (heading+3)%4
#                     # 벽이어서 탐색한 횟수에 1 추가
#                     heading_count += 1
#                     q.append((x,y))
#                 # 왼쪽에 청소가 안되어 있는 곳 발견
#                 if graph[nx][ny] == 0:
#                     #청소하고
#                     visited[nx][ny] = True
#                     #왼쪽으로 방향틀고
#                     heading = (heading+3) % 4
#                     #전진
#                     q.append((nx,ny))
#                     clean += 1

#             # print(heading_count)
#             #네 방향 청소 되어있거나 벽인데 뒤가 벽이 아님. 후진.
#             if heading_count >= 4:
#                 #후진 해야지
#                 if heading == 0 and graph[x-1][y]!=1:
#                     q.append((x-1,y))
#                 if heading == 1 and graph[x][y+1]!=1:
#                     q.append((x,y+1))
#                 if heading == 2 and graph[x+1][y]!=1:
#                     q.append((x+1,y))
#                 if heading == 3 and graph[1][y-1]!=1:
#                     q.append((x,y-1))
        
#             #네 방향 청소 되어있거나 벽인데 뒤가 벽. 작동 중단
#             if heading_count > 10000001:
#                 break

#     return clean

# print(bfs(r,c,d))