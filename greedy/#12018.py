import heapq

ans =0
n ,m=map(int, input().split())
temp = []
for _ in range(n):
    P,L = map(int, input().split())
    mile = list(map(int,input().split()))
    heapq.heapify(mile)
    num = L - P
    if num >0:
        heapq.heappush(temp,1)
    else:
        for i in range(abs(num)):
            heapq.heappop(mile)
        heapq.heappush(temp, heapq.heappop(mile))
while temp:
    mile = heapq.heappop(temp)
    if m - mile >= 0:
        ans+=1
        m-=mile
    else:
        break
print(ans)