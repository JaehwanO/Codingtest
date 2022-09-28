from collections import deque

f, s, g, u, d = map(int,input().split())
visited = [0]*(f+1)
dx = [u,-d]

def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            if 0<nx<(f+1) and visited[nx]==0:
                visited[nx] = visited[x] + 1
                q.append(nx)

# print(bfs(s))
bfs(s)
if visited[g]==0:
    print("use the stairs")
else:
    print(visited[g]-1)