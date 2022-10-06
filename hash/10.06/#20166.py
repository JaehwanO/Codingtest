from collections import deque
n ,m, k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str,input())))

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

candidate = {}
def bfs(a,b):
    q = deque()
    q.append((a,b,graph[a][b]))
    while q:
        x,y,word = q.popleft()
        if word not in candidate:
            candidate[word] = 1
        else:
            candidate[word] += 1
        if len(word) >= 5:
            continue
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == n:
                nx = 0 
            elif nx == -1:
                nx = n-1

            if ny == m:
                ny = 0
            elif ny == -1:
                ny = m-1
            q.append((nx,ny,word+graph[nx][ny]))


ans = []
for i in range(n):
    for j in range(m):
        bfs(i,j)

for _ in range(k):
    god = str(input())

    if god in candidate:
        ans.append(candidate[god])
    else:
        ans.append(0)

for answer in ans:
    print(answer)