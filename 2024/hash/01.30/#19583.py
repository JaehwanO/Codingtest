import sys
input = sys.stdin.readline
def to_second(time):
    x,y = time.split(":")
    return int(x)*60 + int(y)

a,b,c = map(str,input().split())
a = to_second(a)
b = to_second(b)
c = to_second(c)

attend = set()
cnt = 0

while True:
    try:
        time, name = input().split()
        if to_second(time) <= a:
            attend.add(name)
        elif b <= to_second(time) <= c and name in attend:
            attend.remove(name)
            cnt += 1

    except:
        break

print(cnt)