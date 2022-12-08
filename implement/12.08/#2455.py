a,b = map(int,input().split())
ans = 0
for _ in range(3):
    c,d = map(int,input().split())
    b = b-c+d
    ans = max(ans,b)
print(ans)