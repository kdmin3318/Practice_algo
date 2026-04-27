def solution(bandage, health, attacks):
  time = 0
  max = health
  for attack in attacks:
    t, dam = attack
    temp = t-time-1
    n = temp//bandage[0]
    health += n*bandage[2]+temp*bandage[1]
    if health>max: health = max
    health -= dam
    if health<=0: return -1
    time = t
  return health
"""
수학적인 공식을 이용하여 푸는 문제..(별다른 기술 없음)
"""
