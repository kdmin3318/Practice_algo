import sys
input = sys.stdin.readline

from collections import deque

def main():
    n = int(input())
    top = list(map(int, input().split()))
    stack = deque()

    for i in range(n):
        while stack:
            if top[stack[-1]] > top[i]:
                print(stack[-1]+1, end=" ")
                stack.append(i)
                break
            else:
                stack.pop()
        if not stack:
            print(0, end=" ")
            stack.append(i)
    

if __name__ == "__main__":
    main()
