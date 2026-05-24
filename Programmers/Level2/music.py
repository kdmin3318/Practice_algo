def cal_time(time):
  h,m = time.split(":")
  return 60*int(h) + int(m)

def solution(m, musicinfos):
  answer = "(None)"
  temp = {"C#":'c', "D#":'d', "F#":'f', "G#":'g', "A#":'a'}
  max_length = 0
  for a,b in temp.items(): m = m.replace(a,b)
  for info in musicinfos:
    s,e,title,music = info.split(",")
    length = cal_time(e)-cal_time(s)
    for a,b in temp.items(): music = music.replace(a,b)
    n = len(music)
    melody = music*(length//n) + music[:length%n]
    if m in melody and max_length<length:
      answer = title
      max_length = length
  return answer
"""
C#을 소문자 c로 바꾸는 방법 + BF 방식으로 풀이
"""
