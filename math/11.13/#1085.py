x,y,w,h = map(int,input().split())
x_min = min(abs(x-0),abs(w-x))
y_min = min(abs(y-0),abs(h-y))

print(min(x_min, y_min))