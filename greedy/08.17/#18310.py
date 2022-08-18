n = int(input())
l = list(map(int,input().split()))
l.sort()
diff = max(l) - min(l)
if n%2 == 0:
    print(min(l[n//2],l[(n//2)-1]))
else:
    print(l[n//2])