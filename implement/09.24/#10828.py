import sys
answer = []

for i in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().split()
    if x[0] == 'push':
        answer.append(x[1])
    elif x[0] == 'pop':
        if answer:
            print(answer.pop())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(answer))
    elif x[0] == 'empty':
        if answer:
            print(0)
        else:
            print(1)
    elif x[0] == 'top':
        if answer:
            print(answer[-1])
        else:
            print(-1)