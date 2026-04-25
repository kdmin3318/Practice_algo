def solution(s, n);
  answer = ''
  for c in s:
    temp = c
    if c.isupper():
      temp = chr((ord(c)-ord('A')+n)%26 + ord('A'))
    elif c.lower():
      temp = chr((ord(c)-ord('a')+n)%26 + ord('a'))
    answer += temp
  return answer
"""
문자열 <-> 아스키 관련 함수 이용
ord 문자열 -> 아스키
chr 아스키 -> 문자열
!str대신에 chr를 써야한다는 점이 중요함!
"""
