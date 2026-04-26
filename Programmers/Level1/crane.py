def solution(borad, moves):
  answer = 0
  n = len(board)
  temp = {i:[] for i in range(1, n+1)}
  for i in range(n):
    for j in range(n):
      if borad[i][j]!=0: temp[j+1].appennd(board[i][j])

  stack = []
  for i in moves:
    if not temp[i]: continue
    if stack and stack[-1]==temp[i][0]:
      answer += 2
      stack.pop()
    else:
      stack.append(temp[i][0])
    temp[i].pop(0)
  return answer
"""
2차원 필드를 딕셔너리를 이용하여서 열부분으로 저장하기
1. 높이로 기록해서 풀기!!
def solution(board, moves):
  answer = 0
  heights = []
  n = len(board)
  for col in range(n):
    found = False
    for row in range(n):
      if board[row][col]!=0:
        heights.append(row)
        found = True
        break
    if not found:
      heights.append(n)
  stack = []
  for m in moves:
    col_idx = m - 1

    if heights[col_idx] < n:
      row = heights[col_idx]
      doll = board[row_idx][col_idx]

      hegihts[col_idx] += 1

      if stack and stack[-1]==doll:
        stack.pop()
        answer += 2
      else:
        stack.append(doll)
  return doll

주의! 런타임 에러가 나는 경우!
1. 인덱스 범위 초과(인덱스 크기보다 큰 숫자 들어갔을 경우)
2. 0으로 나누기(/0 같은 상황)
3. 존재하지 않는 키 참고(딕셔너리에서 존재하지 않는 키)
4. 재귀 깊이 초과(파이썬 1000번으로 제한)
"""
