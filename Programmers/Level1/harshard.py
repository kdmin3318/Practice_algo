def solution(x):
  def cal(n):
    return sum(int(i) for i in str(n))
  return True if x%cal(x)==0 else False
"""
수학적 정의를 코드로 풀어내기
"""
