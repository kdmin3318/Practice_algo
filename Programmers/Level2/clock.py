def solution(h1,m1,s1,h2,m2,s2):
  answer = 0
  start = h1*3600+m1*60+s1
  end = h2*3600+m2*60+s2
  def get_angles(t):
    h = (t//3600)%12
    m = (t%3600)//60
    s = t%60
    # 초-6도, 분-0.1도, 시-1/120도 소수점 없애기위해 120을 곱
    return s*720 , (m*60+s)*12, (3600*h+60*m+s)
  for t in range(start, end):
    s_cur, m_cur, h_cur = get_angles(t)
    s_next, m_next, h_next = get_angles(t+1)

    match_h = (s_cur<h_cur and s_next>=h_next) or (s_cur<h_cur and s_next==0)
    match_m = (s_cur<m_cur and s_next>=m_next) or (s_cur<m_cur and s_next==0)

    if match_h: answer += 1
    if match_m: answer += 1
    
    if s_next==m_next and s_next==h_next:
      answer -= 1

  start_s, start_m, start_h = get_angles(start)
  if start_s==start_m or start_s==start_h:
    answer += 1
  return answer
"""
시뮬레이션 풀이 방법...
"""
