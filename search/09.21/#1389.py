import sys
from collections import deque

def bfs(x):
    num = [0]*(n+1)
    q = deque()
    q.append(x)
    visited = [x]
    while q:
        a = q.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a]+1
                visited.append(i)
                q.append(i)
    return sum(num)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1,n+1):
    result.append(bfs(i))
print(result.index(min(result))+1)

# n,m,v = map(int,input().split())
# graph = [[] for _ in range(n+1)]

# def dfs(graph,v,visited):
#     visited[v] = True
#     print(v,end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)

# for _ in range(m):
#     a,b=map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# visited = [False] * (n+1)
# dfs(graph,v,visited)