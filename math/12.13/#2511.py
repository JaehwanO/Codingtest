a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_cnt = 0
b_cnt = 0

for i in range(len(a)):
    if a[i] > b[i]:
        a_cnt += 3
    elif a[i] < b[i]:
        b_cnt += 3
    else:
        a_cnt += 1
        b_cnt += 1

if a_cnt > b_cnt:
    print(a_cnt,b_cnt)
    print("A")
if a_cnt < b_cnt:
    print(a_cnt,b_cnt)
    print("B")

if a_cnt == b_cnt:
    print(a_cnt,b_cnt)
    ans = "D"
    for i in range(len(a)-1,-1,-1):
        if a[i] > b[i]:
            ans = "A"
            break
        elif b[i] > a[i]:
            ans = "B"
            break
    print(ans)
