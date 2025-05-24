#include<bits/stdc++.h>
using namespace std;

int board[30][30];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
string a[30];
int b[626];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    int count=0;

    cin>>n;
    for(int i=0;i<n;i++) {
        cin>>a[i];
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            board[i][j] = 0;
        }
    }
    queue<pair<int, int>> Q;
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(a[i][j]=='1'&&board[i][j]==0) {
                int size=0;
                count++;
                board[i][j] = 1;
                Q.push({i,j});
                while(!Q.empty()) {
                    size++;
                    pair<int,int> cur = Q.front();
                    Q.pop();
                    for(int dir=0;dir<4;dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if(nx<0||nx>=n||ny<0||ny>=n) continue;
                        if(board[nx][ny]!=0) continue;
                        if(a[nx][ny]!='1') continue;
                        board[nx][ny]++;
                        Q.push({nx,ny});
                    }
                }
                b[count-1] = size;
            }
        }
    }
    sort(b,b+count);
    cout<<count<<"\n";
    for(int i=0;i<count;i++) {
        cout<<b[i]<<"\n";
    }
    return 0;
}
