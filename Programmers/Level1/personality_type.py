def solution(survey, choices):
    answer = ''
    types = "RTCFJMAN"
    scores = {t: 0 for t in types}
    for i in range(len(survey)):
        score = choices[i]
        if score<4:
            scores[survey[i][0]] += (4-score)
        elif score>4:
            scores[survey[i][1]] += (score-4)
    
    for i in range(0,8,2):
        type_a = types[i]
        type_b = types[i+1]
        if scores[type_a] >= scores[type_b]:
            answer += type_a
        else:
            answer += type_b
    return answer
"""
zip 이용하기!
def solution(survey, choices):
    score_dict = {k: 0 for k in "RTCFJMAN"}

    for (char_a, char_b), choice in zip(survey, choices):
        if choice<4:
            score_dict[char_a] += 4-choice
        elif score>4:
            score_dict[char_b] += choice-4

    indicators = [("R","T"), ("C", "F"), ("J","M"), ("A","N")]

    answer = "".join([a if score_dict[a]>=score_dict[b] else b for a,b in indicators])

    return answer
"""
