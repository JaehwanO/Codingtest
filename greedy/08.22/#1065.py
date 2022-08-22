n = int(input())
s = 0
count = 0
tf = True
for i in range(1,n+1):
    tmp = list(map(int,str(i)))
    if len(tmp)<=2:
            count +=1
    else:
        #tmp[2,1,0]
        diff_1 = tmp[1]-tmp[0]
        for j in range(len(tmp)-1):
            diff_2 = tmp[j+1]-tmp[j]
            if diff_1 == diff_2:
                tf = True
            else: 
                tf = False
                break
            diff_1 = diff_2      
        if tf:
            count +=1
print(count)