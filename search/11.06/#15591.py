from collections import deque

def bfs(start,k):
    cnt = 0
    visited = [False]*(n+1)
    q = deque()
    q.append((start,float('inf')))
    visited[start] = True
    while q:
        v, usado = q.pop()
        for nxt_x , nxt_usado in conn[v]:
            nxt_usado = min(nxt_usado,usado)
            if nxt_usado >= k and not visited[nxt_x]:
                cnt += 1
                q.append((nxt_x,nxt_usado))
                visited[nxt_x] = True

    print(cnt)

n,q = map(int,input().split())
conn = [[] for _ in range(n+1)]
for _ in range(n-1):
    p,q,r = map(int,input().split())
    conn[p].append([q,r])
    conn[q].append([p,r])

for _ in range(q):
    k,start = map(int,input().split())
    bfs(start,k)