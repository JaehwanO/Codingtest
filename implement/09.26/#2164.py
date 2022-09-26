import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = [i for i in range(1,n+1)]
q = deque(q)

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
    # print(q)

print(q[0])