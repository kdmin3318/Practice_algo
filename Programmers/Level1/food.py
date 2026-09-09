def solution(food):
  answer = ''
  for i,f in enumerate(food[1:]):
    answer += str(i+1)*(f//2)
  answer += "0"
  answer += ''.join(list(reversed(answer[:-1])))
  return answer
"""
문자열 합성
"""
