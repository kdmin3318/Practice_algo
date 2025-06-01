#include<bits/stdc++.h>
using namespace std;

int board[302][302];
int vis[302][302];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int bfs(int n, int m) {
    int breg = 0;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            vis[i][j] = 0;
        }
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(board[i][j]>0&&vis[i][j]!=1) {
                vis[i][j] = 1;
                breg++;
                queue<pair<int, int>> Q;
                Q.push({i,j});
                while(!Q.empty()) {
                    pair<int, int> cur = Q.front();
                    Q.pop();
                    for(int dir=0;dir<4;dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if(nx<0||nx>=n||ny<0||ny>=m) continue;
                        if(vis[nx][ny]==1||board[nx][ny]<=0) continue;
                        vis[nx][ny] = 1;
                        Q.push({nx, ny});
                    }
                }
            }
        }
    }
    return breg;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            cin>>board[i][j];
        }
    }
    int year=0;
    while(true) {
        int regions = bfs(n,m);
        if(regions>1) {
            printf("%d", year);
            break;
        } else if(regions==0) {
            printf("0");
            break;
        }
        year++;

        // 임시 배열을 사용해서 동시에 녹이기
        int temp[302][302];
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                temp[i][j] = board[i][j];
            }
        }

        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(board[i][j]>0){
                    int count=0;
                    for(int dir=0;dir<4;dir++) {
                        int nx = i + dx[dir];
                        int ny = j + dy[dir];
                        if(nx<0||nx>=n||ny<0||ny>=m) continue;
                        if(board[nx][ny]<=0) count++;
                    }
                    temp[i][j] = max(0, board[i][j] - count);
                }
            }
        }
        
        // temp 배열을 board로 복사
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                board[i][j] = temp[i][j];
            }
        }
    }
}
