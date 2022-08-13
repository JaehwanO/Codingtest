a = input()
b = input()
cnt = 0

c = a.replace(b,'')

# print(len(c))
# print(len(a))
d=(len(a)-len(c))//len(b)
print(d)
# print(c)
