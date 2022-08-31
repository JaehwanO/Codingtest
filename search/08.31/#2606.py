from collections import deque
computer = int(input())
n = int(input())
graph=[[] for _ in range(computer+1)]
for _ in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
visited = [False]*(computer)
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
bfs(graph,1,visited)
# print()
count = -1
for i in visited:
    if i == True:
        count += 1
print(count)