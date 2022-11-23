from collections import deque

def bfs(graph,s,visited):
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        x = q.popleft()
        print(x,end = " ")
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
n,m,v = map(int,input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


visited = [False] * (n+1)
dfs(graph,v,visited)
visited=[False]*(n+1)
print()
bfs(graph,v,visited)