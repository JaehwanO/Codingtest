num = list(map(int,input().split()))
if sorted(num) == num:
    print("ascending")
else:
    if sorted(num)[::-1] == num:
        print("descending")
    else:
        print("mixed")