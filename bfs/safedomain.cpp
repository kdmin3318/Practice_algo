#include<bits/stdc++.h>
using namespace std;

int board[102][102];
bool vis[102][102];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, h=0;
    int mx=0;
    cin>>n;
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            cin>>board[i][j];
            h = max(h, board[i][j]);
        }
    }
    while(h--) {
        int count=0;
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                if(board[i][j]<h+1) vis[i][j] = 1;
                else vis[i][j] = 0;
            }
        }
        queue<pair<int, int>> Q;
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                if(vis[i][j]==0) {
                    count++;
                    Q.push({i,j});
                    vis[i][j] = 1;
                    while(!Q.empty()) {
                        pair<int, int> cur = Q.front();
                        Q.pop();
                        for(int dir=0;dir<4;dir++) {
                            int nx = cur.first + dx[dir];
                            int ny = cur.second + dy[dir];
                            if(nx<0||nx>=n||ny<0||ny>=n) continue;
                            if(vis[nx][ny]!=0) continue;
                            vis[nx][ny] = 1;
                            Q.push({nx,ny});
                        }
                    }
                }
            }
        }
    mx = max(mx, count);
    }
    cout<<mx;
}
