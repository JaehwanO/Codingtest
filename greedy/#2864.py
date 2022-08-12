a,b=map(str,input().split())
small = 0
big = 0
for _ in range(2):
    if "6" in a or "6" in b:
        a = a.replace("6","5")
        b = b.replace("6","5")
        small= int(a)+int(b)
        # print(small)
        
    elif "5" in a or "5" in b:
        a = a.replace("5","6")
        b = b.replace("5","6")
        big= int(a)+int(b)
        # print(big)
print(small, big)