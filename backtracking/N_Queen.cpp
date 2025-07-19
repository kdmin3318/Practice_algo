#include <bits/stdc++.h>
using namespace std;

bool isused1[40];
bool isused2[40];
bool isused3[40];
int cnt = 0;

void solve(int cur, int n) {
    if(cur==n){
        cnt++;
        return;
    }

    for(int i=0;i<n;i++) {
        if (isused1[i] || isused2[i+cur] || isused3[n-1+cur-i]) continue;
        isused1[i] = 1;
        isused2[cur+i] = 1;
        isused3[n-1+cur-i] = 1;
        solve(cur+1, n);
        isused1[i] = 0;
        isused2[cur+i] = 0;
        isused3[n-1+cur-i] = 0;
    }
}

int main(void) {
    int n;
    cin>>n;
    solve(0,n);
    cout<<cnt;
}
