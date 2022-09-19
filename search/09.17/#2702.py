import math
T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    c = math.gcd(a,b)
    d = math.lcm(a,b)
    print(d,c)