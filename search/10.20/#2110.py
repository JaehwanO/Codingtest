import sys

n, c = map(int,input().split())
l = []

for _ in range(n):
    l.append(int(input()))

l.sort()
start, end = 1, l[-1] - l[0]
# print(l)
result = 0
while start <= end:
    cnt = 1
    mid = (start + end) // 2 
    current = l[0]

    for i in range(1,len(l)):
        if l[i] >= current + mid:
            cnt += 1
            current = l[i]

    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)