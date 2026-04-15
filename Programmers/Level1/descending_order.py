def solution(n):
  answer = 0
  temp = sorted(str(n), reverse=True)
  answer = "".join(temp)
  return int(answer)

"""
한줄로 작성하기
def solution(n):
  answer = int(''.join(sorted(str(n), reverse=True)))
  return answer
중요 포인트
1. .sort()는 '리스트' 전용 메서드
2. sorted()함수는 문자열, 리스트, 튜플 등 모드 사용 가능
3. 내림차순 정리는 reverse=True사용 or 리스트의 경우 [::-1]슬라이싱 이용
"""
