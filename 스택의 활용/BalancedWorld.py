import sys
input = sys.stdin.readline
from collections import deque

def main():
    while True:
        arr = input().rstrip("\n")
        if arr==".":
            break
        
        stack = deque()
        for a in arr:
            balanced = True
            if a=="(" or a=="[":
                stack.append(a)
            elif a==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    balanced = False
                    break
            elif a=="]":
                if stack and stack[-1]=="[":
                    stack.pop()
                else:
                    balanced = False
                    break

        if stack or not balanced:
            print("no")
        else:
            print("yes")

if __name__ =="__main__":
    main()
                
