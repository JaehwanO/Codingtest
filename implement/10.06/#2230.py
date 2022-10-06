import sys

if __name__ == '__main__':
    n, m = map(int,input().split())
    l = [0]*n
    for i in range(n):
        l[i] = int(input())
    l.sort()
    left, right = 0 ,1
    ans = sys.maxsize

    while left < n and right < n:
        diff = l[right]-l[left]

        if diff == m:
            print(m)
            exit(0)
        if diff < m:
            right += 1
            continue
        left += 1 #continue하면 이 코드 생략
        
        ans = min(ans,diff)
print(ans)