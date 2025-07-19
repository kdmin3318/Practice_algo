#include<bits/stdc++.h>
using namespace std;

int n,m;
int arr[10];
int result[10];
bool isused[10];

void solve(int k){
    if(k==m){
        for(int i=0;i<m;i++) cout<<result[i]<<' ';
        cout<<"\n";
        return;
    }

    for(int i=0;i<n;i++){
        if(!isused[i]){
            isused[i] = 1;
            result[k] = arr[i];
            solve(k+1);
            isused[i] = 0;
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>arr[i];
    sort(arr,arr+n);
    solve(0);
}
