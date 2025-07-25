#include<bits/stdc++.h>
using namespace std;

int n, s[10], w[10], ans = 0;

void dfs(int k) {
    if(k == n) {
        int cnt = 0;
        for(int i = 0; i < n; i++) 
            if(s[i] <= 0) cnt++;
        ans = max(ans, cnt);
        return;
    }
    
    if(s[k] <= 0) {
        dfs(k + 1);
        return;
    }
    
    bool canHit = false;
    for(int i = 0; i < n; i++) {
        if(i != k && s[i] > 0) {
            canHit = true;
            s[k] -= w[i]; s[i] -= w[k];
            dfs(k + 1);
            s[k] += w[i]; s[i] += w[k];
        }
    }
    
    if(!canHit) {
        int cnt = 0;
        for(int i = 0; i < n; i++) 
            if(s[i] <= 0) cnt++;
        ans = max(ans, cnt);
    }
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++) cin >> s[i] >> w[i];
    dfs(0);
    cout << ans;
}
