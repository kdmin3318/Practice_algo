from collections import deque
import sys
input = sys.stdin.readline

def main():
    stack = deque()
    n = int(input())
    for _ in range(n):
        s = input().strip().split()
        o = s[0]

        if o =='push':
            stack.append(int(s[1]))
        elif o=='pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif o=='size':
            print(len(stack))
        elif o=='empty':
            print(1 if not stack else 0)
        elif o=='top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        else:
            print("error")
    
if __name__ == "__main__":
    main()
