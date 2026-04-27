def solution(s):
  answer = []
  dic = {}
  for i,c in enumerate(s):
    if c in dic:
      answer.append(i-dic[c])
    else:
      answer.append(-1)
    dic[c] = i
  return answer
"""
딕셔너리를 활용한 문제
"""
