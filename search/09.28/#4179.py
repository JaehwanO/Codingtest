import sys
from collections import deque
input = sys.stdin.readline
 
def bfs():
    while f_queue:    # fire BFS
        x, y = f_queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < R and 0 <= ny < C:
                if not f_visited[nx][ny] and graph[nx][ny] != '#':
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append((nx, ny))
 
    while j_queue:    # jihoon BFS
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < R and 0 <= ny < C:
                if not j_visited[nx][ny] and graph[nx][ny] != '#':
                    if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1:    # important code
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append((nx, ny))
            else:
                return j_visited[x][y] + 1    # escape map
 
    return 'IMPOSSIBLE'    # not escape map
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
f_queue, j_queue = deque(), deque()    # declare fire, jihoon queue
f_visited, j_visited = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]    # declare fire, jihoon visited
 
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            f_queue.append((i, j))
        elif graph[i][j] == 'J':
            j_queue.append((i, j))
print(bfs())


# from collections import deque
# import sys
# input = sys.stdin.readline
# r, c = map(int,input().split())
# graph = []
# for _ in range (r):
#     graph.append(list(input()))
# # print(graph)

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# cnt = 1
# visited = [[False]*c for i in range (r)]

# def bfs(a,b):
#     global cnt, esc
#     q = deque()
#     q.append((a,b))
#     visited[a][b] = True
#     while q:
#         for i in range (r):
#             for j in range(c):
#                 if graph[i][j]=="F":
#                     z, k = i,j
#         x,y = q.popleft()

#         for i in range (4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < r and 0<= ny < c and visited[nx][ny]==False and graph[nx][ny]==".":
#                 graph[nx][ny]="J"
#                 visited[nx][ny]=True
#                 cnt += 1
#                 q.append((ny,ny))
#                 if nx == 0 or nx == r-1 or ny == 0 or ny == c-1:
#                     return True
                
#         # print(graph)
#         for i in range(4):
#             nz = z + dx[i]
#             nk = k + dy[i]
#             if 0 <= nz < r and 0 <= nk < c and graph[nz][nk]!="J":
#                 graph[nz][nk]="F"


# esc = False
# for i in range(r):
#     for j in range(c):
#         if graph[i][j]=="J":
#             if bfs(i,j) == True:
#                 esc = True
#                 print(cnt)
#                 quit(0)
#             else:
#                 esc = False
# if not esc:
#     print("IMPOSSIBLE")