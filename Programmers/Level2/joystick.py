def solution(name):
  temp = [min(ord(c)-ord('A'), ord('Z')-ord(c)+1) for c in name]
  answer = sum(temp)

  n = len(temp)
  move = n-1
  for i in range(n):
    next_i = i+1
    while next_i<n and name[next_i]=='A':
      next_i += 1
    route_a = i + i + (n-next_i) #i까지 갔다가 반대로 돌아가는 경우
    route_b = (n-next_i) + (n-next_i) + i #next_i까지 갔다가 정방향으로 돌아오는 루트
    move = min(move, route_a, route_b)
  answer += move
  return answer
"""
그리디 문제 풀이
'A' 구간을 구한다음 해당 구간을 기준으로
정방향 후 반대 루트, 역방향 후 반대 루트, 쭉 정방향 루트
를 비교했을때 최소 루트가 정답일 것임을 그리디로 확정 짓고 문제 풀이
"""
