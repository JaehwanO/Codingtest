r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
alp_list = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    global cnt
    q = set([(0,0,graph[0][0])])
    while q:
        x,y,z = q.pop()
        cnt = max(cnt,len(z))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny] not in z:
                    q.add((nx,ny,graph[nx][ny]+z))
cnt = 1
bfs()
print(cnt)

# dfs 풀이
# pypy3 성공, python3 2% (시간 초과)
import sys


# # dfs
# def dfs(x, y, z):
#     global cnt

#     # 말이 지날 수 있는 최대의 칸 초기화
#     cnt = max(cnt, z)

#     # 상/하/좌/우 탐색
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         # 범위 내에 있고 탐색하지 않았다면 탐색
#         if 0 <= nx < r and 0 <= ny < c and visited[graph[nx][ny]] == 0:
#             visited[graph[nx][ny]] = 1
#             dfs(nx, ny, z + 1) # 재귀적으로 dfs 탐색
#             visited[graph[nx][ny]] = 0 # 재귀적으로 탐색하는 과정에서 탈출하게 되면 현재의 칸을 탐색 안한걸로 초기화

#     return cnt

# r, c = map(int, sys.stdin.readline().split())
# # 람다 형식으로 문자를 아스키 코드로 바꾼다.
# graph = [list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(r)]
# visited = [0] * 26 # 알파벳 수만큼 생성

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# cnt = 1
# visited[graph[0][0]] = 1
# print(dfs(0, 0, cnt))