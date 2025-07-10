import sys
from collections import deque

def main():
    t = int(input())
    for _ in range(t):
        ac = input().strip()
        n = int(input())
        array_str = input().strip()
        
        # 배열 파싱 개선
        if array_str == "[]":
            dq = deque()
        else:
            x = list(map(int, array_str.strip('[]').split(",")))
            dq = deque(x)
        
        # 뒤집힌 상태를 플래그로 관리 (O(1) 연산)
        reversed_flag = False
        error = False
        
        for op in ac:
            if op == "R":
                reversed_flag = not reversed_flag
            elif op == "D":
                if not dq:
                    print("error")
                    error = True
                    break
                
                # 뒤집힌 상태에 따라 앞/뒤에서 제거
                if reversed_flag:
                    dq.pop()
                else:
                    dq.popleft()
        
        # 에러가 없었다면 결과 출력
        if not error:
            if reversed_flag:
                result = list(reversed(dq))
            else:
                result = list(dq)
            
            print("[" + ",".join(map(str, result)) + "]")

if __name__ == "__main__":
    main()
