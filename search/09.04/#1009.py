t = int(input())
answer = []
for _ in range(t):
    a,b = map(int,input().split())
    n = a**b
    answer.append(n%10)
for i in answer:
    print(i)