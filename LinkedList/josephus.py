from collections import deque

def josephus(n, k):
    dq = deque(range(1, n + 1))
    result = []
    
    while dq:
        dq.rotate(-(k - 1))
        result.append(dq.popleft())
    
    return result

def main():
    n, k = map(int, input().split())
    result = josephus(n, k)
    
    # 훨씬 깔끔한 출력
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    main()
