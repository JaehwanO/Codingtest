n = int(input())
l = list(map(int,input().split()))

def prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

cnt = 0
for i in range(n):
    if prime(l[i]):
        cnt += 1

print(cnt)