#include<bits/stdc++.h>
using namespace std;

int n,m;
int arr[10];
int num[10];
int result[10];

void solve(int k) {
    if(k==m){
        for(int i=0;i<m;i++) cout<<num[arr[i]]<<" ";
        cout<<"\n";
        return;
    }

    int st = 0;
    if(k!=0) st = arr[k-1]+1;
    int temp = 0;
    for(int i=st;i<n;i++){
        if(temp != num[i]){
            result[k] = num[i];
            arr[k] = i;
            temp = result[k];
            solve(k+1);
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>num[i];
    sort(num, num+n);
    solve(0);
}
