#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    
    while(t--) {
        int n;
        cin >> n;
        
        vector<int> arr(n+1);  // 1-indexed
        vector<bool> visited(n+1, false);
        
        // 입력 받기
        for(int i = 1; i <= n; i++) {
            cin >> arr[i];
        }
        
        int cycle_elements = 0;
        
        // 각 원소에서 시작하여 사이클 찾기
        for(int i = 1; i <= n; i++) {
            if(!visited[i]) {
                vector<int> path;
                int curr = i;
                
                // 사이클을 찾을 때까지 경로 따라가기
                while(!visited[curr]) {
                    visited[curr] = true;
                    path.push_back(curr);
                    curr = arr[curr];
                }
                
                // curr이 현재 경로에 있으면 사이클 발견
                auto it = find(path.begin(), path.end(), curr);
                if(it != path.end()) {
                    // 사이클에 속한 원소들의 개수
                    cycle_elements += path.end() - it;
                }
            }
        }
        
        cout << n - cycle_elements << "\n";
    }
    
    return 0;
}
