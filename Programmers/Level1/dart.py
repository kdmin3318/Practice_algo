def solution(dartResult):
  stack = []
  temp = ""
  for d in dartResult:
    if d.isdigit():
      temp += d
    elif d in "SDT":
      score = int(temp)
      if d == "S": stack.append(score ** 1)
      elif d == "D" : stack.append(score ** 2)
      elif d == "T" : stack.append(score ** 3)
      temp = ""
    elif d == "#":
      stack[-1] *= -1
    elif d == "*":
      stack[-1] *= 2
      if len(stack)>=2:
        stack[-2] *= 2
  return sum(stack)
"""
stack을 이용한 풀이, 주의사항으로는 10일때도 포함되기 때문에 isdigit을 이용한 숫자 판별기능 추가
"""
