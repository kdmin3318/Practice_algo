#include<bits/stdc++.h>
using namespace std;

string a[1002];
int b1[1002][1002];
int b2[1002][1002];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin>>n>>m;
    if(n==1&&m==1) {
        cout<<1;
        return 0;
    }
    for(int i=0;i<n;i++) {
        cin>>a[i];
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            b1[i][j] = 0;
            b2[i][j] = 0;
        }
    }
    queue<pair<int, int>> Q1;
    queue<pair<int, int>> Q2;
    Q1.push({0,0});
    Q2.push({n-1,m-1});
    b1[0][0] = 1;
    b2[n-1][m-1] = 1;
    while(!Q1.empty()) {
        pair<int,int> cur = Q1.front();
        Q1.pop();
        for(int dir=0;dir<4;dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if(nx<0||nx>=n||ny<0||ny>=m) continue;
            if(a[nx][ny]=='1'||b1[nx][ny]!=0) continue;
            b1[nx][ny] = b1[cur.first][cur.second] + 1;
            Q1.push({nx,ny});
        }
    }
    while(!Q2.empty()) {
        pair<int,int> cur = Q2.front();
        Q2.pop();
        for(int dir=0;dir<4;dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if(nx<0||nx>=n||ny<0||ny>=m) continue;
            if(a[nx][ny]=='1'||b2[nx][ny]!=0) continue;
            b2[nx][ny] = b2[cur.first][cur.second] + 1;
            Q2.push({nx,ny});
        }
    }
    int path = 1000002;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(a[i][j]=='1') {
                int min1 = 1000002;
                int min2 = 1000002;
                for(int dir=0;dir<4;dir++) {
                    int nx = i + dx[dir];
                    int ny = j + dy[dir];
                    if(nx<0||nx>=n||ny<0||ny>=m) continue;
                    if(a[nx][ny]=='1') continue;
                    if(b1[nx][ny] > 0) min1 = min(min1, b1[nx][ny]);  // 시작점에서 올 수 있는 최단거리
                    if(b2[nx][ny] > 0) min2 = min(min2, b2[nx][ny]);  // 끝점에서 올 수 있는 최단거리
                }
                path = min(path, min1 + min2 + 1);
            }
        }
    }
    if(b1[n-1][m-1]!=0) path = min(path, b1[n-1][m-1]);
    if(path!=1000002) cout<<path;
    else cout<<-1;
}
