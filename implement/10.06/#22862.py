import sys
input = sys.stdin.readline


if __name__=='__main__':
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    m = -(sys.maxsize)

    cnt = 0
    ans = 0
    right = 0
    for left in range(n):

        while cnt <= k and right < n:
            if l[right] % 2 == 1:
                cnt += 1
            else:
                ans += 1
            right += 1

            if left == 0 and right == n:
                m = ans
                break

        if cnt == k+1:
            m = max(ans,m)

        if l[left] % 2 == 1:
            cnt -= 1
            
        else:
            ans -= 1     

print(m)