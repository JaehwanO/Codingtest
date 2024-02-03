n,m = map(int,input().split())
def prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

for num in range(n,m+1):
    if prime(num):
        print(num)
