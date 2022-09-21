import heapq
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))

l.sort()

q =[]
for i in l:
    heapq.heappush(q,i[1])
    if i[0]<len(q):
        heapq.heappop(q)
print(sum(q))