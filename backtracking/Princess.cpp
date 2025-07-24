#include<bits/stdc++.h>
using namespace std;

char board[5][5];
int selected[5][5];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
int cnt = 0;

bool bfs(int x, int y){
    queue<pair<int,int>> Q;
    int vis[5][5] = {0};
    int check = 0;
    int som = 0;  // som을 bfs 함수 내에서 초기화
    
    Q.push({x,y});
    vis[x][y] = 1;
    if(board[x][y]=='S') som++;  // 시작점도 'S' 카운트에 포함
    
    while(!Q.empty()){
        auto [cx, cy] = Q.front();  // 큐에서 현재 좌표를 꺼냄
        Q.pop();
        check++;
        
        for(int dir=0;dir<4;dir++) {
            int nx = cx + dx[dir];  // 현재 좌표 기준으로 이동
            int ny = cy + dy[dir];
            if(nx<0||nx>=5||ny<0||ny>=5) continue;
            if(vis[nx][ny]!=0) continue;
            if(selected[nx][ny]!=1) continue;  // return false 대신 continue
            vis[nx][ny] = 1;
            if(board[nx][ny]=='S') som++;
            Q.push({nx,ny});
        }
    }
    
    if(check==7 && som>=4) return true;
    return false;
}

void solve(int idx, int k){
    if(k==7){
        // 선택된 7개 중 아무 점에서나 BFS 시작 (첫 번째 선택된 점 찾기)
        for(int i=0;i<5;i++){
            for(int j=0;j<5;j++){
                if(selected[i][j]==1){
                    if(bfs(i,j)) cnt++;
                    return;  // 한 점에서만 BFS 실행
                }
            }
        }
        return;
    }
    
    if(idx == 25) return;  // 인덱스 범위 체크
    
    int x = idx / 5;
    int y = idx % 5;
    
    // 현재 위치 선택
    selected[x][y] = 1;
    solve(idx + 1, k + 1);
    selected[x][y] = 0;
    
    // 현재 위치 선택 안함
    solve(idx + 1, k);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++) cin>>board[i][j];
    }
    solve(0, 0);
    cout << cnt << endl;
    return 0;
}
