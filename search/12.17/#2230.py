import sys
if __name__ == '__main__':
    n,m = map(int,input().split())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    left, right = 0, 1
    ans = sys.maxsize
    while right < n and left < n:
        diff = nums[right] - nums[left]
        if diff == m:
            print(m)
            exit(0)
        if diff < m:
            right += 1
            continue
        ans = min(ans,diff)
        left += 1
    print(ans)

