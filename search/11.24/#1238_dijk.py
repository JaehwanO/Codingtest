import heapq
v,e,x = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost))

# start에서 시작해서 다른 노드로 갈 수 있는 최단 거리를 반환한다.
def dijk(start):
    q = []
    distance = [INF] * (v+1)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nxt_node, nxt_cost in graph[now]:
            cost = dist + nxt_cost
            if cost < distance[nxt_node]:
                distance[nxt_node] = cost
            heapq.heappush(q,(cost,nxt_node))
    return distance

result = 0
for i in range(1,v+1):
    go = dijk(i)
    back = dijk(x)
    print(go[x],back[i])
    result = max(result, go[x]+back[i])
print(result)