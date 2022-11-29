import heapq
import sys
input = sys.stdin.readline

# DIJK
def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    # print(distance)
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for n_node,n_cost in graph[now]:
            cost = dist + n_cost
            if cost < distance[n_node]:
                distance[n_node] = cost
                heapq.heappush(q,(cost,n_node))
    return distance

n = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

result = 0 
distance = [INF] * (n+1)
dijk(1)
m = distance.index(max(distance[1:])) 
distance = [INF] * (n+1)
dijk(m)
print(max(distance[1:]))


# # BFS
# from collections import deque
# max_node = -1
# def bfs(start_node):
#     global n, max_node
#     visited =[False]*(n+1)
#     que = deque([[start_node,0]])
#     visited[start_node]=True
#     max_dist = 0

#     while que:
#         now, now_dist = que.popleft()
#         for child,child_dist in data[now]:
#             if not visited[child]:
#                 visited[child]=True
#                 que.append([child,now_dist+child_dist])
#                 if max_dist < now_dist+child_dist:
#                     max_dist = now_dist+child_dist
#                     max_node = child
#     return max_dist
                
# n = int(input())
# if n == 1:
#     print(0)
# else:
#     data = [[] for _ in range(n+1)]
#     for _ in range(n-1):
#         a,b,c = map(int,input().split())
#         data[a].append([b,c])
#         data[b].append([a,c])
#     bfs(1)
#     print(bfs(max_node))

# # DFS
# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# n = int(input())
# graph = [[] for _ in range(n + 1)]


# def dfs(x, wei):
#     for i in graph[x]:
#         a, b = i
#         if distance[a] == -1:
#             distance[a] = wei + b
#             dfs(a, wei + b)


# # 트리 구현
# for _ in range(n - 1):
#     a, b, c = map(int, input().split())
#     graph[a].append([b, c])
#     graph[b].append([a, c])

# # 1번 노드에서 가장 먼 곳을 찾는다.
# distance = [-1] * (n + 1)
# distance[1] = 0
# dfs(1, 0)

# # 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
# start = distance.index(max(distance))
# distance = [-1] * (n + 1)
# distance[start] = 0
# dfs(start, 0)

# print(max(distance))