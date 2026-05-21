def solution(board):
  n = len(board)
  m = len(board[0])
  for i in range(1,n):
    for j in range(1,m):
      if board[i][j]==1:
        board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
  answer = max(max(r) for r in board)**2
  return answer
"""
board에서 1인 부분의 board[i-1][j], board[i][j-1], board[i-1][j-1]의 최솟값
의 +1 만큼 정사각형을 만들 수 있다는 가정에서 출발
DP풀이 방법
"""
