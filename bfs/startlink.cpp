#include<bits/stdc++.h>
using namespace std;

int board[1000002];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int f,s,g,u,d;
    cin>>f>>s>>g>>u>>d;
    for(int i=0;i<f;i++) {
        board[i] = -1;
    }
    if(s==g) {
        cout<<0;
        return 0;
    }
    board[s-1] = 0;
    queue<int> Q;
    Q.push(s-1);
    while(!Q.empty()) {
        int cur = Q.front();
        Q.pop();
        int up = cur + u;
        int down = cur - d;
        if(up<f&&board[up]==-1) {
            board[up] = board[cur] + 1;
            if(up==g-1) {
                cout<<board[up];
                return 0;
            }
            Q.push(up);
        }
        if(down>=0&&board[down]==-1) {
            board[down] = board[cur] + 1;
            if(down==g-1) {
                cout<<board[down];
                return 0;
            }
            Q.push(down);
        }
    }
    cout<<"use the stairs";
    return 0;
}
