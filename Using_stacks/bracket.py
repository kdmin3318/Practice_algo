import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        stack = deque()

        for char in s:
            if char=="(":
                stack.append(char)
            elif char==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(char)
                    break
        
        if stack:
            print("NO")
        else:
            print("YES")
    
if __name__=="__main__":
    main()
