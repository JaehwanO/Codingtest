computer = int(input())
n = int(input())
graph=[[] for _ in range(computer+1)]
for _ in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
visited = [False]*(computer)

def dfs(graph,start,visited):
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)

count = -1
for i in visited:
    if i == True:
        count += 1
print(count)