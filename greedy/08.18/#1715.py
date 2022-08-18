from queue import PriorityQueue
import sys
n = int(sys.stdin.readline())
q = PriorityQueue()
s = 0
l = []
for _ in range(n):
    q.put(int(sys.stdin.readline()))

if q.qsize() ==1:
    print(0)
elif q.qsize() ==2:
    print(q.get()+q.get())

else:
    while q.qsize() != 1:
        s = q.get() + q.get()
        q.put(s)
        l.append(s)
        # print(q.get())
    # print(q.get())
    print(sum(l))
    
# import sys
# from heapq import heapify, heappush, heappop

# input = sys.stdin.readline

# def solve():

#     N = int(input())
#     cards = [int(input()) for _ in range(N)]
#     answer = 0
#     heapify(cards)

#     for _ in range(N - 1):
#         n1 = heappop(cards)
#         n2 = heappop(cards)
#         temp_sum = n1 + n2
#         answer += temp_sum
#         heappush(cards, temp_sum)

#     print(answer)

# solve()