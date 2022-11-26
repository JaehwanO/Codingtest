n = int(input())
for _ in range(n):
    tmp = input()
    alp = tmp.split("-")[0]
    num = tmp.split("-")[1]
    left = 0 
    right = int(num)
    for i in range(3):
        left += (ord(alp[i])-65)*(26**(2-i))
    if abs(left-right) <= 100:
        print("nice")
    else:
        print("not nice")
