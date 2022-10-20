##
import sys
 
if __name__ == "__main__":
    n = int(input())
    l = list(map(int,input().split()))
    left,right = 0, n-1
    ans = l[left] + l[right]
    while left < right:
        tmp = l[left] + l[right]
        if abs(ans) > abs(tmp):
            ans = tmp
        if tmp < 0:
            left += 1
        else:
            right -= 1

    print(ans)