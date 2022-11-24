n = int(input())
my_list = []
for _ in range(n):
    tmp = input()
    have = False

    for word in my_list:
        if tmp in word and len(tmp)*2 == len(word):
            have = True
            break

    if have == False:
        my_list.append(tmp*2)

print(len(my_list))