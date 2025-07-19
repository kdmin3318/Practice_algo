def solve(현재단계):
    if 완료조건:
        결과처리()
        return
    
    for 선택 in 가능한선택들:
        if 유효한선택():
            선택하기()
            solve(다음단계)
            되돌리기()
