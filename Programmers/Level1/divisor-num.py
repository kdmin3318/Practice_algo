def solution(arr, divisor):
  answer = []
  for i in arr:
    if i%divisor==0:
      answer.append(i)
  answer.sort()
  return answer if answer else [-1]
"""
%연산자 이용하여 풀이
1. Pytonic하기 풀이
def solution(arr, divisor):
  answer = sorted([n for n in arr if n%divisor==0])
  return answer if answer else [-1]
주의!
if문과 for문 한줄로 작성하기
- else가 없는 경우에는 for 뒤에 if작성
- else가 있는 경우에는 if else for순으로 작성!
"""
