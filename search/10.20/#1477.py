import sys
input = sys.stdin.readline

n, m, l = map(int,input().split())
highway = [0] + sorted(list(map(int,input().split()))) + [l]

start, end = 0, l-1
result = 0 

while start <= end:
    cnt = 0
    mid = (start+end) // 2

    for i in range(1,len(highway)):
        length = highway[i] - highway[i-1]
        if length > mid:
        
            cnt += (length-1) // mid
    
    if cnt > m:
        start = mid + 1
    else:
        end = mid -1
        result = mid

print(result)
    