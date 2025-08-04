#include<bits/stdc++.h>
using namespace std;

int num[100002];
int d[100002];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin>>n>>m;
    int sum=0;
    d[0] = 0;
    for(int i=0;i<n;i++) {
        cin>>num[i];
        sum+=num[i];
        d[i+1] = sum;
    }

    while(m--){
        int i,j;
        cin>>i>>j;
        cout<<d[j]-d[i-1]<<"\n";
    }
}
