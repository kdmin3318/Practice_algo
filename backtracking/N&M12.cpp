#include<bits/stdc++.h>
using namespace std;

int n,m;
int arr[10];
int num[10];

void solve(int k, int st){
    if(k==m){
        for(int i=0;i<m;i++) cout<<arr[i]<<" ";
        cout<<"\n";
        return;
    }

    int temp = 0;
    for(int i=st;i<n;i++) {
        if(temp != num[i]){
            arr[k] = num[i];
            temp = arr[k];
            solve(k+1,i);
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>num[i];
    sort(num, num+n);
    solve(0,0);
}
