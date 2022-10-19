import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
dp = [0]

for i in range(n):
    low = 0
    high = len(dp) - 1
    while low <= high:
        mid = (low+high) // 2
        if dp[mid] < l[i]:
            low = mid + 1
        else:
            high = mid - 1

    if low >= len(dp):

        dp.append(l[i])
    else:
        dp[low] = l[i]
print(len(dp)-1)