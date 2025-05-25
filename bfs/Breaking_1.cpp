#include<bits/stdc++.h>
using namespace std;

string a[1002];
int board[1002][1002];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++) {
        cin>>a[i];
    }
    queue<pair<int,int>> Q1;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(a[i][j]=='1') Q1.push({i,j});
        }
    }
    Q1.push({0,0});
    int path = 1000002;
    while(!Q1.empty()) {
        pair<int, int> c = Q1.front();
        Q1.pop();
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(c.first==i&&c.second==j) {
                    board[i][j] = 0;
                }
                else board[i][j] = (int)(a[i][j]-'0');
            }
        }
        queue<pair<int, int>> Q2;
        Q2.push({0,0});
        while(!Q2.empty()) {
            pair<int, int> cur = Q2.front();
            Q2.pop();
            for(int dir=0;dir<4;dir++) {
                int nx = cur.first + dx[dir];
                int ny = cur.second + dy[dir];
                if(nx<0||nx>=n||ny<0||ny>=m) continue;
                if(board[nx][ny]!=0)continue;
                board[nx][ny] = board[cur.first][cur.second] + 1;
                Q2.push({nx,ny});
            }
        }
        if(board[n-1][m-1]!=0) path = min(board[n-1][m-1], path);
    }
    if(n==1&&m==1) cout<<1;
    else if(path==1000002) cout<<-1;
    else cout<<path+1;
}
