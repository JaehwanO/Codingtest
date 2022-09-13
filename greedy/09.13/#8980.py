#다시

import sys
input = sys.stdin.readline
 
N, C = map(int, input().split())
M = int(input())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[1])
 
box = [C]*(N+1)
answer = 0
for s, e, b in arr:
    _min = C
    # print(s,e)
    for i in range(s, e):
        _min = min(_min, box[i])
    _min = min(_min, b)
    for i in range(s, e):
        box[i] -= _min
    answer += _min
 
print(answer)