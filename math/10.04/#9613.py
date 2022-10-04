from itertools import permutations
import math
t = int(input())
for _ in range(t):
    ans = 0
    l = list(map(int,input().split()))
    s = permutations(l[1::],2)
    for i in s:
        ans += math.gcd(i[0],i[1])
        # print(i)
    print(ans//2)