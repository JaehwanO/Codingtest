while True:
    s = input()
    if s =='0':
        break
    print("yes") if s == s[::-1] else print("no")