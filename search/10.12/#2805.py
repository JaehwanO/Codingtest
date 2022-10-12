n,m = map(int,input().split())
l = list(map(int,input().split()))
start, end = 1,max(l)

while start <= end:
    mid = (start+end)//2
    height = 0

    for i in l:
        if i >= mid:
            height += (i-mid)

    if height >= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)