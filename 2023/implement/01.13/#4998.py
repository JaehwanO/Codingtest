import sys
try:
    while True:
        cnt =1
        a,b,c=map(float, sys.stdin.readline().split())
        while True:
            if a*(1+b/100) > c: print(cnt); break
            else:
                a*=(1+b/100)
                cnt+=1
except : exit()
