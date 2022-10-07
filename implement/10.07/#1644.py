import sys
input = sys.stdin.readline


if __name__ == '__main__':
    def prime(num):
        if num==1:
            return False
        else:
            for i in range(2, int(num**0.5)+1):
                if num%i == 0:
                    return False
            return True

    n = int(input())
    l = [i for i in range(2,n+1) if prime(i)]
    # print(l)

    right = 0
    s = 0
    cnt = 0
    for left in range(len(l)):
        while right < len(l) and s < n:
            s += l[right]
            right += 1
        if s == n:
            cnt += 1
        s -= l[left]
    print(cnt)