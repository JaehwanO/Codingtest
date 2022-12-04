from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        x = q.popleft()
        for node in conn[x]:
            if not visited[node]:
                visited[node] = True
                q.append(node)

n,m = map(int,input().split())
truth = list(map(int,input().split()))[1:]
visited=[False] * (n+1)
conn = [[] for _ in range (n+1)]
parties = []
for _ in range(m):
    tmp = list(map(int,input().split()))
    num_ppl = tmp[0]
    ppl = tmp[1:]
    parties.append(ppl)
    for i in range(num_ppl):
        for j in range(num_ppl):
            if ppl[i] != ppl[j]:
                conn[ppl[i]].append(ppl[j])
                conn[ppl[j]].append(ppl[i])

for t in truth:
    bfs(t)

not_possible_list = []
for i,v in enumerate(visited):
    if  v:
        not_possible_list.append(i)
ans = 0
for party in parties:
    cnt = True
    for num in party:
        if num in not_possible_list:
            cnt = False

    if cnt:
        ans += 1
print(ans)