def solution(id_list, report, k):
  answer = []
  counter = {name: 0 for name in id_list}
  note = {name: [] for name in id_list}
  email = {name: 0 for name in id_list}
  for r in report:
    a,b = r.split()
    if b in note[a]: continue
    note[a].append(b)
    counter[a] += 1
  for n,c in counter:
    if c<k: continue
    for p,q in note:
      if n in q: email[p]+=1
  for i in email.values():
    answer.append(i)
  return answer
"""
딕셔너리 문제!
1. set을 이용하여서 3중 탐색 부분을 줄이는 방법!
def solution(id_list, report, k):
  report = set(report)

  counter = {name: 0 for name in id_list}
  for r in report:
    _, reported = r.split()
    counter[reported] += 1

  email = {name: 0 for name in id_list}
  for r in report:
    reporter, reported = r.split()
    if counter[reported] >= k:
      email[reporter] += 1

  return [email[name] for name in id_list]
"""
