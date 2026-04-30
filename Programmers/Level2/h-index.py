def solution(citations):
  citations.sort(reverse=True)
  for i,c in enumerate(citations):
    if i+1>c:
      return i
  return len(citations) #예외로 논문 개수보다 모든 논문이 인용 횟수가 더 높다면 모든 논문이 해당
"""
정렬 문제
참고! 내림 차순으로 정렬하면 순서가 논문의 편수가 되는 점을 이용!
"""
