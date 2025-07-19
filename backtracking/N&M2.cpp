#include<bits/stdc++.h>
using namespace std;

int n,m;
int arr[10];

void solve(int k){
    if(k==m){
        for(int i=0;i<m;i++) cout<<arr[i]+1<<' ';
        cout<<"\n";
        return;
    }

    if(k!=0){
        for(int i=arr[k-1]+1;i<n;i++) {
            arr[k] = i;
            solve(k+1);
        }
    }
    else{
        for(int i=0;i<n;i++){
        arr[k]= i;
        solve(k+1);
        }
    }
}

int main(void){
    cin>>n>>m;
    solve(0);
}
