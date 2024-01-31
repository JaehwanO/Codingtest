import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
li = deque([])

for _ in range(1, n + 1):
    li.append(_)

nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    while True:
        if num == li[0]:
            li.popleft()
            break
        else:
            if li.index(num) > len(li) // 2:
                li.appendleft(li.pop())
                cnt += 1
            else:
                li.append(li.popleft())
                cnt += 1

print(cnt)