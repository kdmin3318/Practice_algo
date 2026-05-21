import heapq

def solution(n,k,enemy):
  heap = []
  if k>=len(enemy):
    return len(enemy)
  for idx, e in enumerate(enemy):
    n -= e
    heapq.heappush(heap, -e)
    if n<0:
      if k!=0:
        big_enemy = -heapq.heappop(heap)
        k -= 1
        n += big_enemy
      else:
        return idx
  return len(enemy)
"""
적들의 숫자를 높은 순으로 기록(우선순위 큐)
해둔다음 n이 음수가 될때마다 가장 높은 공격을 무효로 돌리면 최적일것이다 라는 가정에서 출발(그리디!)
우선 순위 큐 + 그리디 문제풀이
"""
