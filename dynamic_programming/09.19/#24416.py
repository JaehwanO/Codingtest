n = int(input())

def fib(n):
    global cnt1
    cnt1 +=1
    if n==1 or n ==2:
        cnt1 -=1
        return 1
    else:
        return fib(n-1) + fib(n-2)

f = [0] * (n+1)

cnt2 = [0]

def fibo(n):
    global cnt2
    f[1] == 1
    f[2] == 1
    for i in range(3,n+1):
        cnt2 +=1
        f[i] = f[i-1] +f[i-2]
    return f[n]


cnt1 ,cnt2 = 0, 0
fib(n)
fibo(n)
print(cnt1+1, cnt2)