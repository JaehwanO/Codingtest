import sys

input = sys.stdin.readline

n,m = map(int,input().split())
uni = []
for _ in range(n):
    tmp = []
    arr = list(map(int, input().split()))
    arr2 = sorted(list(set(arr)))
    dic = {arr2[i] : i for i in range(len(arr2))}
    # print(dic)
    for i in arr:
        tmp.append(dic[i])
    uni.append(tmp)
# print(uni)
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        if uni[i]==uni[j]:
            ans += 1
print(ans)