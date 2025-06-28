#include<bits/stdc++.h>
using namespace std;

int board[102][102];
int vis[102][102];
int dist[102][102];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    for(int i=0;i<n;i++) 
        for(int j=0;j<n;j++) cin>>board[i][j];
    

    queue<pair<int,int>> Q;

    int cnt=0;
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(board[i][j]==0||vis[i][j]) continue;
            cnt++;
            vis[i][j] = 1;
            board[i][j] = cnt;
            Q.push({i,j});
            while(!Q.empty()) {
                pair<int,int> cur = Q.front();
                Q.pop();
                for(int dir=0;dir<4;dir++) {
                    int nx = cur.first + dx[dir];
                    int ny = cur.second + dy[dir];
                    if(nx<0||nx>=n||ny<0||ny>=n) continue;
                    if(board[nx][ny]==0||vis[nx][ny]) continue;
                    board[nx][ny] = cnt;
                    vis[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
        }
    }

    for(int i=0;i<n;i++) fill(dist[i],dist[i]+n,-1);

    int ans = 999999;

    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(board[i][j]!=0){
                Q.push({i,j});
                dist[i][j]=0;
                bool escape = false;
                while(!Q.empty() && !escape) {
                    pair<int, int> cur = Q.front();
                    Q.pop();
                    for(int dir=0;dir<4;dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if(nx<0||nx>=n||ny<0||ny>=n) continue;
                        if(board[i][j]==board[nx][ny]||dist[nx][ny]>=0)continue;
                        if(board[nx][ny] !=0 && board[i][j] != board[nx][ny]) {
                            ans = min(ans, dist[cur.first][cur.second]);
                            while(!Q.empty()) Q.pop();
                            escape = true;
                            break;
                        }
                        dist[nx][ny] = dist[cur.first][cur.second] + 1;
                        Q.push({nx, ny});
                    }
                }
                for(int i=0;i<n;i++) fill(dist[i], dist[i]+n, -1);
            }
        }
    }
    cout<<ans;
}
