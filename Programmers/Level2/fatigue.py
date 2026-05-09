from itertools import permutations

def solution(k, dungeons):
  answer = -1
  for case in permutations(dungeons):
    temp = k
    count = 0
    for required, exhausion in case:
      if required > temp: continue
      temp -= exhausion
      count += 1
    answer = max(answer, count)
  return answer
"""
BF 문제로 모든 경우의 수를 돌면서 답을 구하는 문제(위 풀이에서는 itertools.permutations를 사용
1. Backtracking를 이용한 풀이 방법(DFS+pruning)
def solution(k, dungeons):
    n = len(dungeons)
    visited = [0] * n
    max_count = 0

    def backtrack(current_k, count):
        nonlocal max_count

        max_count = max(max_count, count)
        if max_count==n: return

        for i in range(n):
            if visited[i] or dungeons[i][0] > current_k: continue
            visited[i] = 1
            backtrack(current_k-dungeons[i][1], count+1)
            visited[i] = 0

    backtrack(k, 0)
    return max_count
 """      
