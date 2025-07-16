import sys
input = sys.stdin.readline
from collections import deque

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))

        vis = [False] * n
        cycle_elements = 0

        for i in range(n):
            if not vis[i]:
                path = deque()
                cur = i

                while not vis[cur]:
                    vis[cur] = True
                    path.append(cur)
                    cur = s[cur]-1
                
                if cur in path:
                    idx = path.index(cur)
                    cycle_elements += len(path) - idx

        print(n-cycle_elements)

if __name__ == "__main__":
    main()
