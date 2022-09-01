n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
dfs(graph,v,visited)