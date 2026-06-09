def solution(n,l,r):
  def divide_and_conquer(num,s,e,q_s,q_e):
    if q_e<s or e<q_s: return 0
    if q_s<=s and e<=q_e:
      return 4**num
    if num==0: return 1

    sub_size = 5**(num-1)
    total_ones = 0
    for i in range(5):
      if i==2: continue
      next_s = s+i*sub_size
      next_e = next_s + sub_size-1
      total_ones += divide_and_conquer(num-1, next_s,next_e,q_s,q_e)
    return total_ones
  return divide_and_conquer(n,0,(5**n)-1, l-1, r-1)
"""
분할 정복 문제 풀이 방법...
1. 재귀 풀이방법(for문으로 모든 경우를 돌기 때문에 시간초과가 남)
def solution(n,l,r):
  answer = 0
  def recursion(i,num):
    if num==0: return 1
    temp = 5**(num-1)
    if i//temp==2: return 0
    return recursion(i%temp,num-1)
  for i in range(l-1,r):
    answer += recursion(i,n)
  return answer
"""
