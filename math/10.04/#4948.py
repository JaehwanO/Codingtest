def prime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
dp = []

for i in range(2,246912):
    if prime(i):
        dp.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in dp:
        if n < i <= 2*n:
            cnt +=1
    print(cnt)