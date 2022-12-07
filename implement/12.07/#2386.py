while True:
    n = input()

    if n == "#":
        break
    n = n.lower()
    target = n[0]
    print(target, n[1:].count(target))