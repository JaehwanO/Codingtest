m = int(input())
n = int(input())

ans = []

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for num in range(m,n+1):
    if isPrime(num):
        ans.append(num)
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print("-1")