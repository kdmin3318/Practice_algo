import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    a = list(map(int, input().split()))[::-1]

    stack = deque()
    result = [0 for _ in range(n)]
    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()

        if not stack:
            result[i] = -1
        else:
            result[i] = a[stack[-1]]
        
        stack.append(i)
        
    result.reverse()
    print(" ".join(map(str,result)))

if __name__ == "__main__":
    main()
