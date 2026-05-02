def solution(n):
  answer = 0
  isused1 = [0]*(2*n) # 열 체크
  isused2 = [0]*(2*n) # 대각선 / 방향 체크
  isused3 = [0]*(2*n) # 대각선 \ 방향 체크

  def backtracking(cur, n):
    nonlocal answer
    if cur==n:
      answer += 1
      return 

    for i in range(n):
      if isused1[i] or isused2[cur+i] or isused3[n-1+cur-i]:
        continue
      isused1[i] = 1 # 해당 열 체크
      isused2[cur+i] = 1 # 행과 열을 합한 부분은 모두 / 대각선임
      isused3[n-1+cur-i] = 1 #행과 열을 뺀 부분이 모두 \ 대각선임
      backtracking(cur+1, n)
      isused1[i] = 0
      isused2[cur+i] = 0
      isused3[n-1+cur-i] = 0

  backtracking(0, n)
  return answer
"""
backtracking문제!
N-Queens에서는 특히 cur를 행, i를 열이라 생각하고 대입해서 풀 수 있음
"""
