import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    l = list(map(str,input().split()))
    cnt = 0 
    k = [100001]*n
    # s = ''

    for left in range(n):
        right = left + 1
        # s += l[left]
        k[left]=l[left]
        cnt += 1

        while right < n:
            if l[right] in k:
                break

            if l[left] != l[right] and l[right] not in k:
                cnt += 1
                k[right] = l[right]
                # s += l[right]
                # print(s)
                right +=1

        # s = ''
        k = [100001]*n
    print(cnt)