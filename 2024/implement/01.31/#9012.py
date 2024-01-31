def check(s):
    tmp = []
    for i in s:
        if i == "(":
            tmp.append(i)
        else:
            if tmp:
                tmp.pop()
            else:
                print("NO")
                break
    else:
        if not tmp:
            print("YES")

        else:
            print("NO")

n = int(input())
for _ in range(n):
    task = list(input())
    check(task)
