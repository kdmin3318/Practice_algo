#include<bits/stdc++.h>
using namespace std;

int board[100002];
int dx[2] = {-1,1};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,k;
    cin>>n>>k;
    if(n==k) {
        cout<<0;
        return 0;
    }
    fill(board, board+100001, -1);
    board[n] = 0;
    queue<int> Q;
    Q.push(n);
    while(!Q.empty()) {
        int cur = Q.front(); Q.pop();
        if(k-cur>abs(k-(cur*2))&&cur*2<100000) {
            if(board[cur*2]==-1) board[cur*2] = board[cur];
            else board[cur*2] = min(board[cur], board[cur*2]);
            Q.push(cur*2);
            if(cur*2==k) {
                cout<<board[cur*2];
                return 0;
            }
        }
        for(int dir=0;dir<2;dir++) {
            int nx = cur + dx[dir];
            if(nx<0||nx>100000) continue;
            if(board[nx]!=-1) continue;
            else board[nx] = board[cur] + 1;
            Q.push(nx);
            if(nx==k) {
                cout<<board[nx];
                return 0;
            }
        }
    }
}
