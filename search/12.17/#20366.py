import sys

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    ans = sys.maxsize
    for i in range(N):
        for j in range(i+3,N):
            left = i+1
            right = j-1
            while left < right:
                diff = (arr[i]+arr[j])-(arr[left]+arr[right])
                if abs(ans) > abs(diff):
                    ans = abs(diff)
                if diff < 0:
                    right -= 1
                else:
                    left += 1
    print(ans)