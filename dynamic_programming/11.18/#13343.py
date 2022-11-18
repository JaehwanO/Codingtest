n,m = map(int,input().split())
def gcd(n,m):
    if n < m:
        n,m = m,n
    if n%m == 0:
        return True
    if (n-m<m):
        return not gcd(m,n-m)
    return True

if gcd(n,m):
    print("win")
else:
    print("lose")