import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    picture = [list(input().strip()) for _ in range(n)]
    vis1 = [[0 for _ in range(n)] for _ in range(n)]
    vis2 = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    
    count1 = 0
    count2 = 0
    
    for i in range(n):
        for j in range(n):
            # 정상인의 색 구분
            if vis1[i][j] == 0:
                queue = deque()
                queue.append((i, j))
                vis1[i][j] = 1
                count1 += 1
                current_color = picture[i][j]
                
                while queue:
                    cur = queue.popleft()
                    for dir in range(4):
                        nx = cur[0] + dx[dir]
                        ny = cur[1] + dy[dir]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if picture[nx][ny] != current_color or vis1[nx][ny] != 0:
                            continue
                        queue.append((nx, ny))
                        vis1[nx][ny] = 1
            
            # 색맹인의 색 구분 (R과 G를 같은 색으로 취급)
            if vis2[i][j] == 0:
                queue = deque()
                queue.append((i, j))
                count2 += 1
                vis2[i][j] = 1
                
                while queue:
                    cur = queue.popleft()
                    for dir in range(4):
                        nx = cur[0] + dx[dir]
                        ny = cur[1] + dy[dir]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if vis2[nx][ny] != 0:
                            continue
                        
                        # B는 B끼리만, R과 G는 서로 연결 가능
                        if picture[cur[0]][cur[1]] == "B":
                            if picture[nx][ny] != "B":
                                continue
                        else:  # current_pos_color가 R 또는 G
                            if picture[nx][ny] == "B":
                                continue
                        
                        queue.append((nx, ny))
                        vis2[nx][ny] = 1
    
    print(f"{count1} {count2}")

if __name__ == "__main__":
    main()
