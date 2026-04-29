def solution(answers):
  stu_1 = [1,2,3,4,5]
  stu_2 = [2,1,2,3,2,4,2,5]
  stu_3 = [3,3,1,1,2,2,4,4,5,5]

  test = [0,0,0]

  for i, a in enumerate(answers):
    if stu_1[i%len(stu_1)]==a: test[0]+=1
    if stu_2[i%len(stu_2)]==a: test[1]+=1
    if stu_3[i%len(stu_3)]==a: test[2]+=1

  answer = []
  m = max(test)
  for student in range(3):
    if test[student]==m:
      answer.append(student+1)
  return answer
"""
BF기초 문제, %로 패턴을 제어할 수 있음이 중요함!
"""
