import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
l = list(map(int,input().split()))
l.sort()
cnt = Counter(l)
ans = 0
for i, a in enumerate(l):
    left,right = i+1 , n-1 
    while left < right:
        sum = l[i] + l[left] + l[right]
        if sum == 0:
            if l[left] == l[right]:
                ans += right - left
            else:
                ans += cnt[l[right]]
            left += 1
        
        elif sum > 0:
            right -= 1

        elif sum < 0:
            left += 1
print(ans)