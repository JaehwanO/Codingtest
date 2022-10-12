n = int(input())
l = list(map(int,input().split()))
m = int(input())
s = list(map(int,input().split()))
l.sort()

def search (l,low,high,target):
    if high >= low:
        mid = (high+low)//2
        if l[mid] == target:
            return 1
        
        elif l[mid] > target:
            return search(l,low,mid-1,target)
        else:
            return search(l,mid+1,high,target)
    else:
        return 0

for i in s:
    print(search(l,0,n-1,i),end= ' ')