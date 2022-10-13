n = int(input())
l = list(map(int,input().split()))
m = int(input())
start, end = 1, max(l)

while start <= end:

    mid = (start+end)//2
    revenue = 0

    for i in l:
        if i < mid:
            revenue += i
        else:
            revenue += mid
    
    if revenue <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)