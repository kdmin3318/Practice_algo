def time_cal(t, n):
  h, m = divmod(t, 100)
  a, b = (m+n)//60, (m+n)%60
  return (h+a) + b
def solution(schedules, timelogs, startday):
  answer = 0
  for schedule, log in zip(schedules, timelogs):
    limit = time_cal(schedule, 10)
    s = startday
    possible = True

    for l in log:
      if s<6:
        if l>limit:
          possible=False
          break
        s = (s%7)+1

    if possible: answer += 1
  return answer
"""
문제 내용 그대로 구현 & 시뮬레이션
"""
