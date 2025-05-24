#include<bits/stdc++.h>
using namespace std;

string board[1002];
int s[1002][1002];
int f[1002][1002];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    while(n--) {
        queue<pair<int, int>> Q1;
        queue<pair<int, int>> Q2;
        int w,h;
        cin>>w>>h;
        bool isPossible = false;
        for(int i=0;i<h;i++) {
            cin>>board[i];
        }
        for(int i=0;i<h;i++) {
            for(int j=0;j<w;j++) {
                s[i][j] = -1;
                f[i][j] = -1;
            }
        }
        for(int i=0;i<h;i++) {
            for(int j=0;j<w;j++) {
                if(board[i][j]=='*') {
                    Q1.push({i,j});
                    f[i][j] = 1;
                }
                else if(board[i][j]=='@') {
                    Q2.push({i,j});
                    s[i][j] = 1;
                    if(i==0||i==h-1||j==0||j==w-1) {
                        cout<<1<<"\n";
                        isPossible = true;
                        break;
                    }
                }
            }
            if(isPossible) break;
        }
        if(isPossible) continue;
        //불 경로
        while(!Q1.empty()) {
            pair<int, int> cur = Q1.front();
            Q1.pop();
            for(int dir=0;dir<4;dir++) {
                int nx = cur.first + dx[dir];
                int ny = cur.second + dy[dir];
                if(nx<0||nx>=h||ny<0||ny>=w) continue;
                if(f[nx][ny]!=-1||board[nx][ny]=='#') continue;
                f[nx][ny] = f[cur.first][cur.second] + 1;
                Q1.push({nx,ny});
            }
        }
        //상근이 경로
        while(!Q2.empty()) {
            pair<int, int> cur = Q2.front();
            Q2.pop();
            for(int dir=0;dir<4;dir++) {
                int nx = cur.first + dx[dir];
                int ny = cur.second + dy[dir];
                if(nx<0||nx>=h||ny<0||ny>=w) continue;
                if(s[nx][ny]!=-1||board[nx][ny]=='#') continue;
                if(f[nx][ny]>=0 && s[cur.first][cur.second]+1>=f[nx][ny]) continue;
                s[nx][ny] = s[cur.first][cur.second] + 1;
                Q2.push({nx,ny});
                if(nx==0||nx==h-1||ny==0||ny==w-1) {
                    cout<<s[nx][ny]<<"\n";
                    isPossible = true;
                    break;
                }
            }
            if(isPossible) break;
        }
        if(!isPossible) cout<<"IMPOSSIBLE\n";
    }
    return 0;
}
