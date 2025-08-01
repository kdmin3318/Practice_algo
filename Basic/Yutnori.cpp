#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n=0, arr[4], sum;
    while(n++<3){
        sum = 0;
        for(int i=0;i<4;i++) {
            cin>>arr[i];
            sum += arr[i];
        }
        if(sum==0) cout<<"D\n";
        else if (sum==1) cout<<"C\n";
        else if (sum==2) cout<<"B\n";
        else if (sum==3) cout<<"A\n";
        else if (sum==4) cout<<"E\n";
    }
}
