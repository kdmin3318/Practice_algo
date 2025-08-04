#include<bits/stdc++.h>
using namespace std;

int cost[1002][3];
int d[1002][3];
int n;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n;
    for(int i=1;i<n+1;i++){
        for(int j=0;j<3;j++) cin>>cost[i][j];
    }
    d[1][0] = cost[1][0];
    d[1][1] = cost[1][1];
    d[1][2] = cost[1][2];
    for(int i=2;i<n+1;i++){
        d[i][0] = min(d[i-1][1],d[i-1][2]) + cost[i][0];
        d[i][1] = min(d[i-1][0],d[i-1][2]) + cost[i][1];
        d[i][2] = min(d[i-1][0],d[i-1][1]) + cost[i][2];
    }
    int m = min(d[n][0],d[n][1]);
    m = min(m,d[n][2]);
    cout<<m;
}
