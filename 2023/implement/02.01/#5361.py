import sys
for _ in range(int(sys.stdin.readline())):
    a,b,c,d,e=map(int, sys.stdin.readline().split())
    print("$%.2f"%(a*350.34+b*230.90+c*190.55+d*125.30+e*180.90))
