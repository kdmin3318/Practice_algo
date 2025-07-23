#include<bits/stdc++.h>
using namespace std;

int k;
int num[15];
int arr[10];

void solve(int a, int st){
    if(a==6){
        for(int i=0;i<6;i++) cout<<arr[i]<<" ";
        cout<<"\n";
        return;
    }
    for(int i=st;i<k;i++) {
        arr[a] = num[i];
        solve(a+1,i+1);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    while(1){
        cin>>k;
        if(k==0) break;
        for(int i=0;i<k;i++) cin>>num[i];
        sort(num,num+k);
        solve(0,0);
        cout<<"\n";
    }
}
