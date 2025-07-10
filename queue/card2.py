import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    queue = deque()
    for i in range(1,n+1):
        queue.append(i)
    while not len(queue)==1:
        queue.popleft()
        queue.rotate(-1)
    print(queue.popleft())

if __name__ =="__main__":
    main()
