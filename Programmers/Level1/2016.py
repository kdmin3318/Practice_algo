def solution(a, b);
  month = [31,29,31,30,31,30,31,31,30,31,30,31]
  days = ['THU','FRI','SAT','SUN','MON','TUE','WED']

  n = sum(month[:a-1])
  n += b

  return days[n%7]
"""
누적합 문제(BF 문제)
"""
