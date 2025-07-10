import sys
input = sys.stdin.readline
from collections import deque

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    c_queue = deque()
    for i in range(1,n+1):
        c_queue.append(i)
    
    count = 0
    for number in a:
        target_index = c_queue.index(number)
        while c_queue[0]!=number:
            if target_index > len(c_queue)//2:
                c_queue.rotate(1)
                count += 1
            else:
                c_queue.rotate(-1)
                count += 1
        c_queue.popleft()

    print(count)

if __name__ =="__main__":
    main()
