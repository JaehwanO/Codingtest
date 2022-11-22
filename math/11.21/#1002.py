import math
t = int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if d == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) < d < (r1+r2):
        print(2)
    elif abs(r1-r2) == d or r1+r2 == d:
        print(1)
    else:
        print(0)