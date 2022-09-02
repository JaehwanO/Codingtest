from collections import deque
import sys
input = sys.stdin.readline
dx = [-2,-1,1,2,-2,1,-1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(a,b,c,d):
    q = deque()
    q.append([a,b])
    visited[a][b]=1
    while q:
        x,y = q.popleft()
        if x==c and y == d:
            print(visited[end_x][end_y]-1)
            return 
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < l and 0<= ny < l and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                q.append([nx,ny])

t = int(input())
for _ in range(t):
    l = int(input())
    start_x,start_y=map(int,input().split())
    end_x,end_y=map(int,input().split())
    visited = [[0]*l for _ in range(l)]
    bfs(start_x,start_y,end_x,end_y)