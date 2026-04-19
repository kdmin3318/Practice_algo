def timer1(time):
  h, m = map(int, time.split(":"))
  return h*60 + m
def timer2(time):
  return f"{time//60:02d}:{time%60:02d}"

def solution(video_len, pos, op_start, op_end, commands):
  video_len = timer1(video_len)
  pos = timer1(pos)
  op_start = timer1(op_start)
  op_end = timer1(op_end)

  if pos>=op_start and pos<=op_end:
    pos = op_end

  for commmand in commands:
    if command=="next":
      pos = min(video_len, pos+10)
    elif command=="prev":
      pos = max(0, pos-10)
    if pos>=op_start and pos<=op_end:
      pos = op_end
  return timer2(pos)
"""
시간<->숫자 함수를 생성할 수 있고, min,max 기본 함수를 잘 활용하여 풀이
1. 모든 시간 한번에 변경 방법
  video_len, pos, op_start, op_end = map(timer1, [video_len, pos, op_start, op_end])
"""
