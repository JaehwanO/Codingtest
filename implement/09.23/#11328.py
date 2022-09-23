N = int(input())
 
for i in range(N):
    a, b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
 
    if len(a) != len(b):
        print("Impossible")
        continue
 
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = False
            break
        else:
            flag = True
            
    if flag:
        print("Possible")
    else:
        print("Impossible")
