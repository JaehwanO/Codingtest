target = ['U', 'C', 'P', 'C']
n = input()
r = ''

for x in n:
  c = x
  if c == 'U' or c == 'C' or c == 'P':
    r += c

i = 0
l = ''

for x in r:
  if l == 'UCPC':
    break
  elif x == target[i]:
    l += x
    i += 1
    
if l == 'UCPC':
  print('I love UCPC')
else:
  print('I hate UCPC')