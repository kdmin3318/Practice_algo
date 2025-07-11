import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    count = 0
    for _ in range(n):
        s = input().strip()
        stack = deque()
        for w in s:
            if stack and stack[-1]==w:
                stack.pop()
            else:
                stack.append(w)
            
        if not stack:
            count += 1

    print(count)
            
if __name__ =="__main__":
    main()
