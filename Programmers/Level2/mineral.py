import math

def cal_fatigue(pick, mineral):
  if pick=="D":
    return 1
  elif pick=="I":
    if mineral=="diamond": return 5
    else: return 1
  elif pick=="S":
    if mineral=="diamond": return 25
    elif mineral=="iron": return 5
    else: return 1

def solution(picks, minerals):
  n = sum(picks)
  cnt = math.ceil(len(minerals)/5)
  temp = []
  for i, p in enumerate(picks):
    if i==0:
      for _ in range(p): temp.append("D")
    elif i==1:
      for _ in range(p): temp.append("I")
    else:
      for _ in range(p): temp.append("S")

  if n>cnt: n=cnt
  score = {i:0 for i in range(n)}
  for i, mineral in enumerate(minerals):
    if i//5==n: break
    if mineral=="diamond": score[i//5] += 25
    elif mineral=="iron": score[i//5] += 5
    elif mineral=="stone": score[i//5] += 1

  score = sorted(score.items(), key=lambda x:x[1], reverse=True)
  answer = 0
  for pick, s in enumerate(score):
    for mineral in minerals[s[0]*5:s[0]*5+5]:
      answer += cal_fatigue(temp[pick], mineral)
  return answer
"""
시뮬레이션 + 그리디 풀이 방법
가장 피로도가 높은 구간을 찾아두고 높은 구간 부터 가장 좋은 곡괭이를 쓰는것이 최소화하는 최선의 선택임을 가정하고 출발
DFS와 Pruning을 활용한 풀이 법도 존재할 수 있음
"""
