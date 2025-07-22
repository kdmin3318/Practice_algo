#include<bits/stdc++.h>
using namespace std;

int n,m;
int num[10];
int arr[10];

void solve(int k){
    if(k==m){
        for(int i=0;i<m;i++) cout<<num[arr[i]]<<" ";
        cout<<"\n";
        return;
    }
    
    int st = 0;
    if(k!=0) st = arr[k-1];
    for(int i=st;i<n;i++){
        arr[k] = i;
        solve(k+1);
    }
}

int main(void) {
    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>num[i];
    sort(num, num+n);
    solve(0);
}
