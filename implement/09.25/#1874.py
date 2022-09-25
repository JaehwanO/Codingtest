n = int(input())
s = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)

# n = int(input())
# ori = []
# l = []
# for _ in range(n):
#     l.append(int(input()))
# s = 0
# num = 1
# sign =[]
# while s !=n:
#     if num > n+1:
#         print("NO")
#         quit(0)
#     if l[s] not in ori:
#         ori.append(num)
#         num += 1
#         sign.append("+")
#         # print("+")
#     if l[s] in ori:
#         s += 1
#         ori.pop()
#         # print("-")
#         sign.append("-")

# for i in sign:
#     print(i)
