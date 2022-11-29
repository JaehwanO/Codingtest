import heapq
import sys
input = sys.stdin.readline
n = int(input())

q = []

for _ in range(n):
    op = int(input())
    if not q and op == 0:
        print("0")
    elif q and op == 0:
        print(heapq.heappop(q))
    elif op != 0:
        heapq.heappush(q,op*(1))
