#include<bits/stdc++.h>
using namespace std;

int board[102][102];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int a[102];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int count=0;
    int m,n,k;
    cin>>m>>n>>k;
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++) {
            board[i][j] = 0;
        }
    }
    while(k--) {
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        for(int i=b;i<d;i++) {
            for(int j=a;j<c;j++) {
                board[i][j]++;
            }
        }
    }
    queue<pair<int, int>> Q;
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++) {
            if(board[i][j]==0) {
                int mass=0;
                count++;
                board[i][j]++;
                Q.push({i,j});
                while(!Q.empty()) {
                    mass++;
                    pair<int, int> cur = Q.front();
                    Q.pop();
                    for(int dir=0;dir<4;dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if(nx<0||nx>=m||ny<0||ny>=n) continue;
                        if(board[nx][ny]!=0) continue;
                        board[nx][ny]++;
                        Q.push({nx,ny});
                    }
                }
                a[count-1] = mass;
            }
        }
    }
    cout<<count<<"\n";
    sort(a, a+count);
    for(int i=0;i<count;i++) cout<<a[i]<<" ";
}
