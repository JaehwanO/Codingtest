t = int(input())
for _ in range(t):
    cnt = 0
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    for _ in range(n):
        # -5 1
        # -3 -1 1
        px,py,pr = map(int,input().split())
        d1 = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5
        d2 = (((x2 - px) ** 2) + ((y2 - py) ** 2)) ** 0.5

        if (d1 < pr and d2 > pr) or (d1 > pr and d2 < pr):
            cnt += 1    
    print(cnt)