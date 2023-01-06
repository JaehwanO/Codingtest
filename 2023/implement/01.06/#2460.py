m = 0
now = 0
for _ in range(10):
    down,up = map(int,input().split())
    now -= down
    now += up
    m = max(m,now)
print(m)