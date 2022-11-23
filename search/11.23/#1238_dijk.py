import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    distance = [INF] * (v + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance

result = 0
for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)


# def dijkstra(start):
#     q = []
#     distance = [INF] * (v+1)
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dist,now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
        
#         for next_node, next_cost in graph[now]:
#             cost = dist + next_cost
#             if distance[next_node] > cost:
#                 distance[next_node] = cost
#                 heapq.heappush(q,(cost,next_node))
#     return distance