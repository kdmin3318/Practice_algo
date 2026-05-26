def solution(rows, columns, queries):
  answer = []
  board = [[0]*columns for _ in range(rows)]
  for i in range(rows):
    for j in range(columns):
      board[i][j] = i*columns+j+1
  for query in queries:
    x1,y1,x2,y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
    temp = board[x1][y1]
    min_val = temp
    #왼쪽
    for i in range(x1,x2):
      board[i][y1] = board[i+1][y1]
      min_val = min(min_val, board[i][y1])
    #아래쪽
    for j in range(y1,y2):
      board[x2][j] = board[x2][j+1]
      min_val = min(min_val, board[x2][j])
    #오른쪽
    for i in range(x2,x1,-1):
      board[i][y2] = board[i-1][y2]
      min_val = min(min_val, board[i][y2])
    #위쪽
    for j in range(y2,y1,-1):
      board[x1][j] = board[x1][j-1]
      min_val = min(min_val, board[x1][j])
    board[x1][y1+1] = temp
    answer.append(min_val)
  return answer
"""
BF + 시뮬레이션 문제 풀이!
"""
