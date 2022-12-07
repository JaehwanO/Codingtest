n,m = map(int,input().split())
graph =[[]] + [[0]*(i+1) for i in range(n+1)]
graph[1][0] = 1
graph[2][0] = 1
graph[2][1] = 1

for i in range(3,n+2):
    for j in range(len(graph[i])):
        if j == 0:
            graph[i][0] = 1
        elif j == len(graph[i])-1:
            graph[i][len(graph[i])-1] = 1
        elif 0<j and j<len(graph[i]):
            graph[i][j] = graph[i-1][j-1] + graph[i-1][j]

print(graph[n+1][m])