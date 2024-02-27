while True:
  str = input()
  check = [] #괄호를 체크하기 위한 배열
  answer = 'yes'
  if str == '.':
    break
  for s in str:
    if s=='(' or s=='[': #열린 괄호가 들어오면 check 배열에 추가한다
      check.append(s)
    elif s == ')':
      if not len(check): # '(' 괄호가 나오기 전에 ')' 괄호가 나온 경우
        answer = 'no'
        break
      else:
        if check.pop(-1) != '(':
          answer = 'no'
          break
    elif s == ']':
      if not len(check): # '[' 괄호가 나오기 전에 ']' 괄호가 나온 경우
        answer = 'no'
        break
      else:
        if check.pop() != '[':
          answer = 'no'
          break
    else:
      continue
  if len(check): #괄호 검사가 끝나고 난 후에도 배열에 괄호가 남아있는 경우
    answer = 'no'
  print(answer)