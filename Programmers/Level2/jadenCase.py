def solution(s):
  answer = []
  for c in s.split(' '):
    answer.append(c.capitalize())
  return " ".join(answer)
"""
capitalize 함수 활용!
1. 슬라이싱을 활용한 문제 풀이
def solution(s):
  answer = []
  for w in s.split(' '):
    if w:
      new_word = w[0].upper() + w[1:].lower()
      answer.append(new_word)
    else:
      answer.append('')
  return " ".join(answer)
"""
