t = int(input())
for _ in range(t):
    n = int(input())
    l = [False]*(n+1)

    for i in range(1,n+1):
        for j in range(1,n+1):
            turn  = i*j
            if turn <= n:
                if l[turn] == False:
                    l[turn] = True
                else:
                    l[turn] = False                 

    ans = l.count(True)
    print(ans)