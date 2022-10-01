from sys import*
input = stdin.readline
def regist(arr):
    for x in arr:
        temp=''
        temp=x[::-1]
        res.append(int(temp))
          
a=list(map(str,input().split()))
n=int(a[0])
res=[]
if len(a)>1:
    regist(a[1:])
while 1:
    inp=list(map(str,input().split()))
    regist(inp)
    if len(res)==n: break
res.sort()
for i in range(n):
    print(res[i])