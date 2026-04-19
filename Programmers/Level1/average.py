def soulution(arr):
  answer = sum(arr)/len(arr)
  return answer
"""
sum과 len 기본함수를 활용하여 풀이
주의!
배열이 비었을 경우가 있다면 조건을 추가해주는 것이 좋음
return answer if arr else 0
"""
