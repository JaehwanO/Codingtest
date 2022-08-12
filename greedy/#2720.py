T = int(input())
for _ in range(T):
    my = [0]*4
    money = int(input())
    while money != 0:
        if money >= 25:
            my[0]=money//25
            money -= 25*(money//25)
        elif money >= 10:
            my[1]=money//10
            money -= 10*(money//10)
        elif money >= 5:
            my[2]=money//5
            money -= 5*(money//5)
        elif money >= 1:
            my[3]=money//1
            money -= 1*(money//1)
    print(my[0],my[1],my[2],my[3])
    
    # if __name__ == '__main__':
    #     for _ in range(int(input())):
    #     c = int(input())

    #     print(c // 25, end=' ')
    #     c %= 25
    #     print(c // 10, end=' ')
    #     c %= 10
    #     print(c // 5, end=' ')
    #     c %= 5
    #     print(c // 1)
# 
