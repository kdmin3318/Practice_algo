def solution(elements):
  n = len(elements)
  elements = elements*2
  s = set()
  for i in range(n):
    for j in range(i+1, i+1+n):
      s.add(sum(elements[i:j]))
  return len(s)
"""
set()함수 활용, BF풀이 방법
"""
