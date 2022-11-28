x,y = map(int,(input().split()))
thirtyone = [1,3,5,7,8,10]
thirty = [4,6,9,11]
weekend = {1:"MON", 2:"TUE", 3:"WED", 4:"THU",5:"FRI",6:"SAT",0:"SUN"}
days = 0
for m in range(1,x):
    if m in thirtyone:
        days += 31
    elif m in thirty:
        days += 30
    elif m == 2:
        days += 28

days += y
print(weekend[days%7])

