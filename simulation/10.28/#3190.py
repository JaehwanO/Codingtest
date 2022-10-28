import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[0]*n for _ in range (n)]
k = int(input())
for _ in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

l = int(input())
command_time = []
command_type = []
for _ in range(l):
    a,b = map(str,input().split())
    command_time.append(int(a))
    command_type.append(b)

command_time = command_time[::-1]
command_type = command_type[::-1]
#   왼 아래 오른 위
dx = [0,1,0,-1]
dy = [1,0,-1,0]


x_head,y_head = 0,0
x_tail,y_tail = 0,0
direc = 0
time = 0
nx,ny = 0,0
tail_list = deque()
# print(command_time)
while True:
    if time in command_time:
        command_time.pop()
        tmp = command_type.pop()

        if tmp == "D":
            direc = (direc+1) % 4
 
            
        elif tmp == "L":
            direc = (direc-1) % 4
 

    nx = x_head + dx[direc]
    ny = y_head + dy[direc] 

    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        break
    
    elif graph[nx][ny] == 5:
        break

    elif 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
        tail_list.append((nx,ny))
        graph[x_tail][y_tail] = 0
        x_head = nx
        y_head = ny
        graph[x_head][y_head] = 5
        x_tail, y_tail = tail_list.popleft()

    elif 0<=nx<n and 0<=ny<n and graph[nx][ny] != 0:
        tail_list.append((nx,ny))
        x_head = nx
        y_head = ny
        graph[x_head][y_head] = 5
        graph[x_tail][y_tail] = 5

    time += 1
    # print(graph)
print(time+1)