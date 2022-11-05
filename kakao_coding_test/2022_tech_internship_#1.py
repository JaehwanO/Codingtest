import heapq
def solution(n, paths, gates, summits):
    conn =[[] for _ in range(n+1)]
    for i,j,w in paths:
        conn[i].append((j,w))
        conn[j].append((i,w))
    # 다익스트라
    pq  = [(0,gate) for gate in gates]
    MAX = 10000001
    min_dist = [MAX for _ in range(n+1)]
    
    while pq:
        intensity, node = heapq.heappop(pq)
        if min_dist[node] <= intensity:
            continue
        min_dist[node] = intensity
        if node in summits:
            continue
        for nxt_n, nxt_w in conn[node]:
            nxt_w = max(intensity,nxt_w)
            if min_dist[nxt_n] <= nxt_w:
                continue
            heapq.heappush(pq,(nxt_w,nxt_n))
    ans = [0,MAX]
    for summit in summits:
        if min_dist[summit] < ans[1]:
            ans[0] , ans[1] = summit,min_dist[summit]
        elif min_dist[summit] == ans[1] and summit<ans[0]:
            ans[0] = summit
    return ans