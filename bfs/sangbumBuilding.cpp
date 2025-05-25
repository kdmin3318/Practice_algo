#include<bits/stdc++.h>
using namespace std;

int dz[6] = {1,-1,0,0,0,0};
int dx[6] = {0,0,1,0,-1,0};
int dy[6] = {0,0,0,1,0,-1};
int board[32][32][32];
string a[32][32];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while(1) {
        int l,r,c;
        cin>>l>>r>>c;
        if(l==0&&r==0&&c==0) break;
        bool isEscaped = false;
        for(int i=0;i<l;i++) {
            for(int j=0;j<r;j++) {
                cin>>a[i][j];
            }
        }
        queue <tuple<int, int, int>> Q;
        for(int i=0;i<l;i++) {
            for(int j=0;j<r;j++) {
                for(int k=0;k<c;k++) {
                    if(a[i][j][k]=='S') {
                        board[i][j][k] = 0;
                        Q.push({i,j,k});
                    }
                    else board[i][j][k] = -1;
                }
            }
        }
        while(!Q.empty()) {
            tuple<int, int, int> cur = Q.front();
            Q.pop();
            for(int dir=0;dir<6;dir++) {
                int nz = get<0>(cur) + dz[dir];
                int nx = get<1>(cur) + dx[dir];
                int ny = get<2>(cur) + dy[dir];
                if(nz<0||nz>=l||nx<0||nx>=r||ny<0||ny>=c) continue;
                if(board[nz][nx][ny]!=-1||a[nz][nx][ny]=='#') continue;
                board[nz][nx][ny] = board[get<0>(cur)][get<1>(cur)][get<2>(cur)] + 1;
                if(a[nz][nx][ny]=='E') {
                    cout<<"Escaped in "<<board[nz][nx][ny]<<" minute(s).\n";
                    isEscaped = true;
                    break;
                }
                Q.push({nz,nx,ny});
            }
        }
        if(!isEscaped) cout<<"Trapped!\n";
    }
}
