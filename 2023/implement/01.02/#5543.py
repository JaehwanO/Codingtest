ham, drink = int(1e9), int(1e9)
for _ in range(3):
    ham = min(ham,int(input()))

for _ in range(2):
    drink = min(drink,int(input()))
print(ham+drink-50)
