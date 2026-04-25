def solution(numbers. hand):
  answer = ''
  left, right = 10, 12

  for n in numbers:
    if n==0: n=11

    temp = ""
    if n in [1,4,7]:
      temp = 'L'
    elif n in [3,6,9]:
      temp = 'R'
    else:
      dist_l = abs((n-1)//3 - (left-1)//3) + abs((n-1)%3 - (left-1)%3)
      dist_r = abs((n-1)//3 - (right-1)//3) abs((n-1)%3 - (right-1)%3)
      if dist_l > dist_r:
        temp = 'R'
      elif dist_l < dist_r:
        temp = 'L'
      else:
        temp = 'R' if hand=="right" else 'L'

    if temp=="R": right = n
    else: left = n
    answer += temp

  return answer
"""
키패트 숫자를 좌표화 시켜서 서리를 생각하는 것이 중요 포인트.. bfs의 기초 연습문제
"""
