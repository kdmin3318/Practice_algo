#include <bits/stdc++.h>
using namespace std;

int arr[20];
int cnt = 0;
int n, s;


void solve(int k, int result){
    if(k==n){
        if(result==s) cnt++;
        return;
    }
    
    solve(k+1, result);
    solve(k+1, result+arr[k]);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>s;
    for(int i=0;i<n;i++) cin>>arr[i];
    solve(0,0);
    if(s==0) cnt--;
    cout<<cnt;
}
