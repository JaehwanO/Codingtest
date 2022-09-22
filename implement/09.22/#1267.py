n = int(input())
l = list(map(int,input().split()))
m = 0
y = 0

for i in l:
    y += (i//30)*10
    m += (i//60)*15
    if i%30>=0:
        y+=10
    if i%60>=0:
        m+=15

if m>y:
    print("Y", y)
elif m<y:
    print("M", m)
else:
    print("Y", "M", y)