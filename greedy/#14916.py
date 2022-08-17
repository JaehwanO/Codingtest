money = int(input())
n = 0
while money != 0:
    if money < 5 and money%2!=0:
        n = -1
        break
    elif money % 5!= 0:
         n += 1
         money -= 2
    elif money % 5 == 0:
        n+=1
        money -= 5
print(n)