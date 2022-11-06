import sys
from collections import deque


def find_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != ".":
                bomb_list.append((i,j))


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def all_zero():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != "O":
                graph[i][j] = "O"


def bamb():
    while bomb_list:
        x,y = bomb_list.popleft()
        graph[x][y] = "."
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < r and 0<=ny < c:
                if graph[nx][ny] == "O":
                    graph[nx][ny] = "."

r, c, n = map(int, sys.stdin.readline().split())
# 1단계: 폭탄을 설치
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

# 2단계: 봄버맨은 아무것도 하지 않는다.
n -= 1
while n:
    # 폭탄의 위치를 저장할 리스트
    bomb_list = deque()

    # 폭탄의 위치 저장
    find_bomb()

    # 3단계: 모든 칸의 폭탄을 설치
    all_zero()

    n -= 1
    if n == 0:
        break

    # 4단계: 3초전에 설치된 폭탄 폭발
    bamb()
    n -= 1

for i in graph:
    print("".join(i))