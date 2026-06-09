def solution(record):
  answer = []
  name = {}
  logs = []
  for r in record:
    arr = r.split(" ")
    if arr[0]!="Change":
      logs.append((arr[1], arr[0]))
    if arr[0]!="Leave":
      name[arr[1]] = arr[2]
  for u,s in logs:
    if s=="Enter": answer.append(f"{name[u]}님이 들어왔습니다.")
    else: answer.append(f"{name[u]}님이 나갔습니다.")
  return answer
"""
딕셔너리 + 시뮬레이션 문제!
"""
