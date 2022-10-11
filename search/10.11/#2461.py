import sys
import heapq
from collections import deque

input = sys.stdin.readline().rstrip()
n, m = map(int,input().split())
student = [deque(sorted(list(map(int,input().split())))) for _ in range(n)]
heap = []

min_value = int(10e9)
max_value = 0

for i in range(len(student)):
    v = student[i].popleft()
    max_value = max(max_value,v)
    min_value = min(min_value,v)
    heapq.heappush(heap,[v,i])

ans = max_value - min_value

while heap:
    prev_min , pos = heapq.heappop(heap)
    
    if not student[pos]:
        break
    
    new_value = student[pos].popleft()
    heapq.heappush(heap,[new_value,pos])

    if max_value < new_value:
        max_value = new_value
    min_value = heap[0][0]
    ans = min(ans,max_value-min_value)
    
# import sys
# import heapq
# from collections import deque
 
# input = lambda : sys.stdin.readline().rstrip()
 
# n, m = map(int, input().split())
# students = [deque(sorted(list(map(int, input().split())))) for _ in range(n)]
 
# heap = []
 
# min_value = int(10e9)
# max_value = 0
 
# for i in range(len(students)):
#     v = students[i].popleft()
#     max_value = max(max_value, v)
#     min_value = min(min_value, v)
#     heapq.heappush(heap, [v, i])
 
# sumation = max_value - min_value

# while heap:
#     prev_min_value, pos = heapq.heappop(heap)

#     if not students[pos]:
#         # 해당 deque가 비어있다면 더이상 갱신 불가능
#         break
 
#     new_value = students[pos].popleft()
#     heapq.heappush(heap, [new_value, pos])
 
#     if max_value < new_value:
#         max_value = new_value
#     min_value = heap[0][0]
#     sumation = min(sumation, max_value - min_value)
 
 
# print(sumation)