def solution(n, lost, reserve):
  cloth = [1]*n
  for l in lost:
    cloth[l-1]-=1
  for r in reserve:
    cloth[r-1]+=1
  for i in range(n):
    if cloth[i]==2:
      if i>0 and cloth[i-1]==0:
        cloth[i-1]+=1
        cloth[i]-=1
      elif i<n-1 and cloth[i+1]==0:
        cloth[i+1]+=1
        cloth[i]-=1
  answer = sum(1 for n in cloth if n>=1)
  return answer
"""
앞의 순서를 먼저 채우면 뒷 사람의 기회가 생길 수 있다는 초급 그리디 풀이 방법!
"""
