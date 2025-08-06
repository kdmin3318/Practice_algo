#include<bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin>>t;
    vector<pair<int,int>> d;
    d.push_back({1,0});
    d.push_back({0,1});
    while(t--){
        int n;
        cin>>n;
        int s = int(d.size());
        if(n>=s){
            for(int i=s;i<=n;i++){
                int count_0 = d[i-1].first+d[i-2].first;
                int count_1 = d[i-1].second+d[i-2].second;
                d.push_back({count_0,count_1});
            }
        }
        cout<<d[n].first<<" "<<d[n].second;
        cout<<"\n";
    }
}
