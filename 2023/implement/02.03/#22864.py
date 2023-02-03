a, b, c, m = map(int, input().split())

day = 0

result = 0
count = 0

if a > m :
  print(0)
else :
  while day != 24 :
    day += 1
    if count + a <= m :
      result += b
      count += a
    else :
      if count - c >= 0 :
        count -= c
      else :
        count = 0

  print(result)