m,n = map(int,input().split())
l = list(map(int,input().split()))
start,end = 1, max(l)

while start <= end:
    mid = (start+end)//2
    cnt = 0

    for i in l:
        if i >= mid:
            cnt += i//mid
            
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)