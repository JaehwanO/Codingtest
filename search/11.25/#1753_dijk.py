import heapq
import sys
input = sys.stdin.readline
def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for n_node,n_cost in graph[now]:
            cost = dist + n_cost
            if cost < distance[n_node]:
                distance[n_node] = cost
                heapq.heappush(q,(cost,n_node))

v,e = map(int,input().split())
k = int(input())

INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
dijk(k)
for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])