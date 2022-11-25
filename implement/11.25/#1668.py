n = int(input())
tro = list(int(input()) for _ in range(n))
ans = tro[0]
cnt = 1
for i in range(1,n):
    if tro[i] > ans:
        cnt += 1
        ans = tro[i]
print(cnt)

ans = tro[n-1]
cnt = 1
for i in range(n-2,-1,-1):
    if tro[i] > ans:
        cnt += 1
        ans = tro[i]
print(cnt)