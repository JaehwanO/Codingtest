from collections import defaultdict

n = int(input())
fr = list(list(input()) for _ in range(n))

visited = [[False]*n for _ in range(n)]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if fr[i][j] == "Y" or (fr[i][k] == "Y" and fr[j][k] == "Y"):
                visited[i][j] = True


result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if visited[i][j]:
            cnt += 1
    result = max(result, cnt)

print(result)