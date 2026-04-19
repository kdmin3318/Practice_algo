def solution(phone_number):
  answer = "*"*(len(phone_number)-4) + phone_number[-4:]
  return answer
"""
문자열도 list처럼 활용이 가능함!
"""
