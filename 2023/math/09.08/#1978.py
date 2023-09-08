n = int(input())
num = list(map(int,input().split()))
cnt = 0

def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
    return True
for i in range(n):
    if prime(num[i]):
        cnt += 1

print(cnt)