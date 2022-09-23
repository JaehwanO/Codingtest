n,k = map(int,input().split())
room = [[0]*6 for i in range(2)]
ans = 0 
for _ in range(n):
    a,b = map(int,input().split())
    room[a][b-1]+=1

for i in room[0]:
    if i !=0 and i<=k:
        ans+=1
    if i!=0 and i>k:
        ans += int(i//k)
        i = i%k
        if i!=0 and i < k:
            ans+=1

for i in room[1]:
    if i !=0 and i<=k:
        ans+=1
    if i!=0 and i>k:
        ans += int(i//k)
        i = i%k
        if i!=0 and i < k:
            ans+=1
print(room)
print(ans) 