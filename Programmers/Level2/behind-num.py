def solution(numbers):
  answer = []
  stack = []
  while numbers:
    while stack and stack[-1]<=numbers[-1]:
      stack.pop()
    if not stack:
      answer.append(-1)
    else:
      answer.append(stack[-1])
    stack.append(numbers.pop())
  answer.reverse()
  return answer
"""
stack 풀이 방법!
"""
