import heapq
import sys
import heapq

input = sys.stdin.readline

leftheap = []
rightheap = []

n = int(input())
for _ in range(n):
    num = int(input())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap,-num)
    else:
        heapq.heappush(rightheap,num)
    
    # 균형유지
    if rightheap and rightheap[0] < -leftheap[0]:
        leftval = heapq.heappop(leftheap)
        rightval = heapq.heappop(rightheap)

        heapq.heappush(leftheap,-rightval)
        heapq.heappush(rightheap,-leftval)

print(-leftheap[0]) 