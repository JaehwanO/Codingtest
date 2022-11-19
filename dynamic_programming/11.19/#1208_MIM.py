import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int,input().split())

l = list(map(int,input().split()))

left_half = l[:n//2]
right_half = l[n//2:]

tmp_left = []
tmp_right = []

for i in range(len(left_half)+1):
    comb = combinations(left_half,i)
    for i in comb:
        tmp_left.append(sum(i))

for i in range(len(right_half)+1):
    comb1 = combinations(right_half,i)
    for i in comb1:
        tmp_right.append(sum(i))

tmp_left.sort()
tmp_right.sort()

left = 0 
right = len(tmp_right) - 1
ans = 0

while left < len(tmp_left) and right >= 0:
    tmp = tmp_left[left] + tmp_right[right]

    if tmp == s:
        same_count_left = 1
        same_count_right = 1

        left_idx = left
        right_idx = right

        left += 1
        right -= 1
        while left < len(tmp_left) and tmp_left[left] == tmp_left[left_idx]:
            same_count_left += 1
            left += 1
        
        while right >= 0 and tmp_right[right] == tmp_right[right_idx]:
            same_count_right += 1
            right -= 1        
        ans += same_count_right * same_count_left

    elif tmp < s:
        left += 1

    elif tmp > s:
        right -= 1

if s == 0 :
    ans -= 1

print(ans)