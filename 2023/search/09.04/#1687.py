from collections import deque
n, k = map(int,input().split())

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[k])
            break
        for j in (x-1,x+1, x*2):
            if 0<=j<=MAX and not dist[j]:
                dist[j] = dist[x] + 1
                q.append(j)
MAX = 100000
dist = [0]*(MAX+1)
bfs()