from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0] == 'push_back':
        q.append(x[1])

    elif x[0] == 'push_front':
        q.appendleft(x[1])

    elif x[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif x[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(q))
    elif x[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif x[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

        
