def solution(absolutes, signs):
  answer = 0
  for a,s in zip(absolutes, signs):
    if s: answer+=a
    else: answer-=a
  return answer
"""
zip 기본 함수 활용!
1. sum함수를 추가로 이용!
def solution(absolutes, signs):
  return sum(a if s else -a for a,s in zip(absolutes, signs))
"""
