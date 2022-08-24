l =[]
answer = []
for _ in range(9):
    l.append(int(input()))
# print(l)
for i in range(8):
    for j in range(i+1,9):
         first = l[i]
         second = l[j]
         answer = sum(l)-first-second
         if answer == 100:
            a = first
            b = second 
            break
l.remove(a)
l.remove(b)
for i in l:
    print(i)
    # print(sum(i))
    