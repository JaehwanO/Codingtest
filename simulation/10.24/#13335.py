##
import sys

n, w, l = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
temp = [0] * w 
cnt = 0

while temp:
    cnt += 1 
    temp.pop(0) 

    if a:
        if sum(temp) + a[0] > l:
            temp.append(0)

        else:
            temp.append(a.pop(0))

print(cnt)