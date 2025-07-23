#include<bits/stdc++.h>
using namespace std;

int n,m;
int num[10];
int arr[10];
bool used[10];

void solve(int k) {
    if(k==m){
        for(int i=0;i<m;i++) cout<<arr[i]<<" ";
        cout<<"\n";
        return;
    }

    int temp = 0;
    for(int i=0;i<n;i++) {
        if(!used[i] && temp != num[i]){
            used[i] = 1;
            arr[k] = num[i];
            temp = arr[k];
            solve(k+1);
            used[i] = 0;
        }
    }
}

int main(void) {
    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>num[i];
    sort(num, num+n);
    solve(0);
}
