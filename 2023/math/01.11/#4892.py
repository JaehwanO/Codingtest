n = 0

while True:
    n += 1
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3*n0
    if n1%2==0:
        n2 = n1//2
    else:
        n2 = (n1+1)//2
    n3 = 3*n2
    n4 = n3//9
    
    if n1%2 == 0:
        print(f"{n}. even {n4}")
    else:
        print(f"{n}. odd {n4}")
        
        
