def solution(n, m, section):
  answer = 0
  last = 0
  for s in section:
    if last<s:
      last = s+m-1
      answer += 1
  return answer
