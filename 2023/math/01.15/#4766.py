tmp = float(input())
while True:
    n = float(input())
    if n == 999:
        break
    print(f'{n-tmp:.2f}')
    tmp = n 