def time_to_m(time):
  h,m = map(int, time.split(":"))
  return h*60+m

def solution(fees, records):
  answer = []
  car = {}
  basic, bf, h, hf = fees
  for record in records:
    t, c, state = record
    if state=="IN":
      car[c] = car.get(c,0) - time_to_m(t)
    else:
      car[c] = car.get(c,0) + time_to_m(t)
  car = sorted(car.items(), key=lambda x: x[0])
  for c,time in car:
    if time<=0:
      time += time_to_m("23:59")
    park = time
    if park<=basic:
      answer.append(bf)
    else:
      answer.append(bf+(park-basic+h-1)//h*hf)

  return answer
"""
시뮬레이션 문제! 딕셔너리 해시 활용
1. 딕셔너리도 pop이 가능한 점을 이용!
import math

def solution(fees, records):
  basic_time, basic_fee, unit_time, unit_fee = fees

  parking = {}
  total_times = {}

  for record in records:
    time_str, car_id, state = record.split()
    h, m = map(int, time_str.split(":"))
    minutes = h*60 + m

    if state=="IN":
      parking[car_id] = minutes
    else:
      duration = minutes - parking.pop(car_id) #pop하면 value를 반환함!
      total_times[car_id] = total_times.get(car_id, 0) + duration

  last_time = 23*60 + 59
  for car_id, in_time in parking.items():
    total_times[car_id] = total_times.get(car_id, 0) + (last_time - in_time)

  answer = []
  for car_id in sorted(total_times.keys()):
    time = total_times[car_id]

    if time<=basic_time:
      fee = basic_fee
    else:
      extra_time = time-basic_time
      fee = basic_fee + math.ceil(extra_time/unit_time)*unit_fee

    answer.append(fee)
  return answer
"""
