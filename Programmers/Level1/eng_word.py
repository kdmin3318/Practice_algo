def solution(s):
  card = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
  for eng, num in card.items():
    s = s.replace(eng, str(num))
  return int(s)
"""
replace() 함수 활용 문제
"""
