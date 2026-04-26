def solution(data, ext, val_ext, sort_by):
  answer = []
  temp = {s:i for i,s in enumerate(["code","date","maximum","remain"])}

  j = temp[ext]
  for i in data:
    if i[j]<val_ext:
      answer.append(i)

  k = temp[sort_by]
  answer = sorted(answer, key=lambda x: x[k])
  return answer
"""
sorted의 기준을 key로 정할 수 있음!
"""
