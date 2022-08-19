import sys

s = list(str(sys.stdin.readline()))
# \n 제거
s.pop()
ascii_code = []
reverse = []
result = ""

# 문자를 아스키 코드로 변환
for i in s:
    ascii_code.append(ord(i))

# 초기 타겟
target = ascii_code[0]
reverse.append(target)

# 반복문을 통해 작은 수를 뒤로 보낸다.
for i in range(1, len(s)):
    # 타겟과 현재 아스키 코드 비교
    if target < ascii_code[i]:
        # 현재 아스키 코드가 크므로 한번 뒤집어준다.
        reverse.reverse()
        # 현재 아스키 코드를 추가하고 다시 뒤집어 작은 수를 뒤로 보낸다.
        reverse.append(ascii_code[i])
        reverse.reverse()
    else:
        # 타겟이 더 크면 타겟을 현재 아스키 코드로 바꾼다.
        target = ascii_code[i]
        # 현재 아스키 코드를 추가한다.
        reverse.append(ascii_code[i])

# 아스키 코드를 문자로 변환해서 문자열로 만든다.
# 문자열은 다시 뒤집어 줘야하기때문에 뒤집어서 반복한다.
for i in reversed(reverse):
    result += chr(i)

print(result)

# import sys

# s = str(input())
# first = s
# second = ''
# answer = []
# answer.append(s)

# for i in range(len(s)):
#     s = first
#     for j in range(i+1, len(s)):
#         second = s[j::-1] + s[j+1::]
#         s = second
#         # print(second)
#         answer.append(second)
# print(str(min(answer)))