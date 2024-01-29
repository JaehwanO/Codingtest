from collections import deque

q = [i+1 for i in range(int(input()))]
q = deque(q)

while len(q) > 1:
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)

print(q.pop())
