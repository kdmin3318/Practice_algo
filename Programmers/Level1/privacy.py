def solution(today, terms, privacies):
  answer = []

  def day_cal(n):
    y,m,d = map(int, n.split("."))
    return y*28*12 + m*28 + d

  today = day_cal(today)

  t = {}
  for term in temrs:
    a,b = term.split()
    t[a] = int(b)*28

  for i, privacy in enumerate(privacies):
    day, term = privacy.split()
    day_lit = day_cal(day) + t[term]
    if today>=day_lit:
      answer.append(i+1)
    
  return answer
"""
총일수를 계산하는 함수를 이용하여 풀이
"""
