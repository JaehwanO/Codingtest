n = int(input())
graph = [[0]*101 for _ in range(101)]
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            graph[i][j] = 1
ans = 0
for i in graph:
    ans += i.count(1)
print(ans)