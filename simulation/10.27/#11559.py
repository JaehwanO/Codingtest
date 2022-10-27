from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if s[j][i] != "." and s[k][i] == ".":
                    s[k][i] = s[j][i]
                    s[j][i] = "."
                    break


def bfs(i, j, char):
    q = deque()
    q.append([i, j])
    chain.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and visit[nx][ny] == 0 and s[nx][ny] == char:
                visit[nx][ny] = 1
                q.append([nx, ny])
                chain.append([nx, ny])

s = [list(input().strip()) for i in range(12)]
result = 0
while True:
    isTrue = False
    visit = [[0] * 6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if s[i][j] != "." and visit[i][j] == 0:
                visit[i][j] = 1
                chain = []
                bfs(i, j, s[i][j])
                if len(chain) > 3:
                    isTrue = True
                    for x, y in chain: s[x][y] = "."
    if not isTrue: break
    down()
    result += 1
print(result)

# import sys
# from collections import deque, Counter
# input = sys.stdin.readline
# bbu_list = ['R','G','B','Y']

# graph = [list(map(str,input().rstrip())) for _ in range(12)]
# # print(graph)

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def pop(a,b):
#     visited = [[False]*6 for i in range(12)]
#     bbu = graph[a][b]
#     q = deque()
#     pop_cordinate = []
#     cnt = 1
#     q.append((a,b))
#     pop_cordinate.append((a,b))
#     visited[a][b] = True

#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<12 and 0<=ny<6:
#                 if visited[nx][ny] == False and graph[nx][ny] == bbu:
#                     visited[nx][ny] = True
#                     cnt += 1
#                     pop_cordinate.append((nx,ny))
#                     q.append((nx,ny))
#     if cnt >= 4:
#         return pop_cordinate
#     else:
#         return False
#     # print(cnt)

# def remove_bbu(l):
#     for i in l:
#         graph[i[0]][i[1]] = '.'

# # def put_down(l):

# #     #밑에서부터 한줄씩 서치해서 밑에 빈공간있으면 내리기
# #     for j in range(6):
# #         fill_in = []
# #         bbu_ = []
# #         for i in range(11,-1,-1):
# #             if l[i][j] == '.':
# #                 fill_in.append((i,j))
# #             elif l[i][j]!='.' and fill_in:
                
# #                 bbu_.append(graph[i][j])
# #                 graph[i][j] = '.'

            
# #         bbu_[::-1]
# #         if bbu_:
# #             for i in range(len(bbu_)):
# #                 x,y = fill_in[i][0],fill_in[i][1]
# #                 graph[x][y] = bbu_.pop()
# def down():
#     for i in range(6):
#         for j in range(10, -1, -1):
#             for k in range(11, j, -1):
#                 if graph[j][i] != "." and graph[k][i] == ".":
#                     graph[k][i] = graph[j][i]
#                     graph[j][i] = "."
#                     break


# ans = 0
# for i in range(12):
#     for j in range(6):
#         if graph[i][j] in bbu_list:
#             tmp = pop(i,j)
#             if tmp:
#                 remove_bbu(tmp)
#                 # print(graph)
#                 down()
#                 # print(graph)
#                 ans += 1
# print(ans)