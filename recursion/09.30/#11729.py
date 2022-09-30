n = int(input())
print((1<<n)-1)
#원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법
def hanoi(a,b,n):
    if n == 1:
        print(a, b)
        return
    hanoi(a,6-a-b,n-1)
    print(a, b)
    hanoi(6-a-b,b,n-1)

hanoi(1,3,n)