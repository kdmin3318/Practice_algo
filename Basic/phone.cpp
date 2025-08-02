#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    int y=0,m=0;
    while(n--){
        int temp;
        cin>>temp;
        y+=10*(temp/30+1);
        m+=15*(temp/60+1);
    }
    if(y<m) cout<<"Y "<<y;
    else if(m<y) cout<<"M "<<m;
    else cout<<"Y M "<<y;
}
