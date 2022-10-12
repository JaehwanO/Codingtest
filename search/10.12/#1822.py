n,m = map(int,input().split())
l = list(map(int,input().split()))
s = list(map(int,input().split()))
s.sort()
l.sort()
ans = []
def search (l,low,high,target):
    if high >= low:
        mid = (high+low)//2
        if l[mid] == target:
            return True
        
        elif l[mid] > target:
            return search(l,low,mid-1,target)
        else:
            return search(l,mid+1,high,target)
    else:
        return False

for i in l:
    if not search(s,0,m-1,i):
        ans.append(i)

if ans:
    print(len(ans))
    for i in ans:
        print(i,end=' ')
else:
    print(0)