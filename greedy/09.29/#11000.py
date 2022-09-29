import heapq
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]: 
        heapq.heappush(room, q[i][1])
    else: 
        heapq.heappop(room) 
        heapq.heappush(room, q[i][1])

print(len(room))


# import sys
# input = sys.stdin.readline
# n = int(input())
# start = []
# end = []
# for _ in range(n):
#     a,b = map(int,input().split())
#     start.append(a)
#     end.append(b)    
# # print(start)
# # print(end)
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if start[i]==end[j]:
#             start[i]=1000000001
#             end[j] = 1000000001
#             cnt += 1
#             # print(cnt)

# print(n-cnt)