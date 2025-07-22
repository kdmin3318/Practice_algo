#include<bits/stdc++.h>
using namespace std;

int n,m;
int arr[10];
int result[10];
bool used[10];

void solve(int k){
    if(k==m){
        for(int i=0;i<m;i++){
            cout<<result[i]<<" ";
        }
        cout<<"\n";
        return;
    }

    int st = 0;
    if(k != 0) {
    for (int j = 0; j < n; j++) {
        if (arr[j] == result[k - 1]) {
            st = j;
            break;
            }
        }
    }

    for(int i=st;i<n;i++){
        if(!used[i]){
            result[k] = arr[i];
            used[i] = 1;
            solve(k+1);
            used[i] = 0;
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>arr[i];
    sort(arr,arr+n);
    solve(0);
}
