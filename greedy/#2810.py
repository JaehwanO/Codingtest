# N = int(input())
# s = str(input())
# new = s.replace("LL","S")
# count = new.count("S")
# if count == 2:
#     print("2")
# elif count == 1:
#     print("1")
# else:      
#     print(count+1)
N = int(input())
member = input()
count = member.count('LL')
if (count <= 1):
    print(len(member))

else:
    print(len(member) - count + 1)