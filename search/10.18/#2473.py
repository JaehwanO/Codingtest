import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
l = list(map(int,input().split()))
# s = l
l.sort()

ans = sys.maxsize

for i, num in enumerate(l):
    left,right = i+1 , n-1 
    
    while left < right:
        tmp = l[left] + l[right] + l[i]
        if ans > abs(tmp):
            ans = abs(tmp)
            result = [l[i],l[left],l[right]]

        if tmp < 0:
            left += 1

        elif tmp > 0:
            right -= 1
        else:
            break
print(result[0],result[1],result[2])