num = list(map(int,input().split()))
num = list(map(lambda x : x**2,num))
print(sum(num)%10)