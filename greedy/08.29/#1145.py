from itertools import permutations
import math
l= list(map(int,input().split()))
answer = []
a ,b = 1000000000, 100000000000000
for i in range(len(l)-2):
    for j in range(i+1, len(l)-1):   
        for k in range(j+1, len(l)):
            # print(l[i],l[j],l[k])   
            a = math.lcm(l[i],l[j],l[k])
            answer.append(min(a,b))
            b = a
print(min(answer))