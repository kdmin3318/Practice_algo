from collections import Counter

def solution(X, Y):
  common = Counter(X) & Counter(Y)
  temp = sorted(common.elements(), reverse=True)
  if not temp: answer="-1"
  elif temp[0]=="0": answer="0"
  else:
    answer = "".join(temp)
  return answer
"""
Counter 활용 문제
"""
