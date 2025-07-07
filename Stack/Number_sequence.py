import sys
input = sys.stdin.readline

from collections import deque

def main():
    n = int(input())
    t = deque()
    for i in range(n,0,-1):
        t.append(i)

    stack = deque()
    result = []
    for _ in range(n):
        k = int(input())
        count = 0

        while not stack or k > stack[-1]:
            if not t:
                print("NO")
                return
            stack.append(t.pop())
            count += 1
        
        if stack and k==stack[-1]:
            stack.pop()
            result.append(count)
        else:
            print("NO")
            return
    
    for count in result:
        for _ in range(count):
            print("+")
        print("-")
        
if __name__ == "__main__":
    main()
