def solution(keymap, targets):
  answer = []
  d = {}
  for key in keymap:
    for i, c in enumerate(key):
      d[c] = (d.get(c,101), i+1)
  for target in targets:
    temp = 0
    for c in target:
      if not c in d:
        temp = -1
        break
      temp += d[c]
    answer.append(temp)
  return answer
"""
딕셔너리 활용해서 서칭 시간 줄이고 풀기!
참고! index()써도 시간 초과가 걸리지는 않음
"""
