def is_prime(n):
  prime = True
  if n<=1: return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      prime = False
      break
  return prime

def solution(n):
  answer = sum(1 for i in range(1,n+1) if is_prime(i))
  return answer
"""
소수 서칭의 최적화
참고! 위의 풀이법은 단일이 소수임을 서칭하는데는 최적인 방법이지만 전범위를 커버하는 것은 에라토스테의 체가 더 좋음
1. 에라토스테의 체(O(nlog(logn)) 압도적으로 빠름
def solution(n):
  prime = [1] * (n+1) #기본적으로 모든수를 소수라고 봄
  prime[0]=prime[1]=0 #0,1는 소수가 아님
  for i in range(2,int(n**0.5)+1):
    if prime[i]: #i가 소수라면
      for j in range(i*i, n+1, i):
        prime[j] = 0
  return sum(prime)
"""
