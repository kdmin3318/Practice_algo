def solution(land):
  n = len(land)
  for i in range(1,n):
    land[i][0] += max(land[i-1][1:])
    land[i][1] += max([land[i-1][0]] + land[i-1][2:])
    land[i][2] += max(land[i-1][:2] + [land[i-1][3]])
    land[i][3] += max(land[i-1][:3])
  return max(land[n-1])
"""
DP풀이 방법..
참고! DP는 점화식을 세워야하기 떄문에 i가 나오려면 i-1에 뭘 하면되는지를 생각하는 것이 좋음!
"""
