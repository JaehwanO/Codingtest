import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    distance = [INF] * (n+1)
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nxt_node,nxt_cost in graph[now]:
            cost = dist + nxt_cost
            if cost < distance[nxt_node]:
                distance[nxt_node] = cost
            heapq.heappush(q,(cost,nxt_node))

    return distance

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    s,end,c = map(int,input().split())
    graph[s].append((end,c))
    graph[end].append((s,c))

v1,v2 = map(int,input().split())

one = dijk(1)
v1_ = dijk(v1)
v2_ = dijk(v2)

ans = min(one[v1]+v1_[v2]+v2_[n],one[v2]+v2_[v1]+v1_[n])
print(ans if ans < INF else -1)