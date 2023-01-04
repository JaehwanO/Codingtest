while True:
    try:
        word = input()
        lower = 0
        upper = 0
        num = 0
        empty = 0
        for i in word:
            if i.isalpha():
                if i == i.lower():
                    lower += 1
                elif i == i.upper():
                    upper += 1
            elif i.isnumeric():
                num+=1
            elif i == ' ':
                empty+=1
        print(lower, upper,num,empty)

    except:
        break