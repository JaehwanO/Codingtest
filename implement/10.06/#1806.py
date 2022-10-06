import sys
input = sys.stdin.readline
ans = sys.maxsize

if __name__ == '__main__':
    n,s = map(int,input().split())
    l = list(map(int,input().split()))

    right = 0 
    summ = 0

    for left in range(n):
        while right < n and summ < s:
            summ += l[right]
            right += 1
        if summ >= s:
            # print(left,right)
            ans = min(ans,(right-left))
        summ -= l[left]
        
if ans == sys.maxsize:
    print(0)
else:
    print(ans)
