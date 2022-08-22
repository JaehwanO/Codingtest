p,k = map(int,input().split())
l=[]
for i in range(1,p+1):
    if p%i ==0:
        l.append(i)
if l:
    if len(l)<k:
        print(0)
    else:    
        print(l[k-1])
else:
    print(0)