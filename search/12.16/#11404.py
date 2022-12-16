n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int,input().split())
    if graph[s][e] > c:
        graph[s][e] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0,end = ' ')
        else:
            print(graph[i][j],end=' ')
    print()