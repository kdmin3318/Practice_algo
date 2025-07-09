import sys
input = sys.stdin.readline

from collections import deque

def main():
    n = int(input())
    h = [int(input()) for _ in range(n)]
    h.append(1000000002)
        
    stack = deque()
    result = 0
    for i in range(n+1):
        while stack and h[stack[-1]] <= h[i]:
            result += i-stack.pop()-1
        stack.append(i)

    print(result)


if __name__ == "__main__":
    main()
