from collections import deque
n = int(input())
graph = [[] for i in range(n+1)]
x,y = map(int,input().split())
m = int(input())
visited = [0]*(n+1)
res = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start]=1
    while q:
        v = q.popleft()
        # print(v,end=' ')
        for i in graph[v]:
            if visited[i]==0:
                q.append(i)
                res[i] = res[v] +1
                visited[i] = 1
bfs(x)
if res[y]>0:
    print(res[y])
else:
    print(-1)