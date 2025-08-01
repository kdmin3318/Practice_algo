#include<bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a[9] = {};
    for(int i=0;i<9;i++) cin>>a[i];
    sort(a,a+9);
    int brute[9] = {0,0,0,0,0,0,0,1,1};
    do{
        int sum=0;
        for(int i=0;i<9;i++){
            if(brute[i]==0) sum+=a[i];
        }
        if(sum==100){
            for(int i=0;i<9;i++){
            if(brute[i]==0) cout<<a[i]<<"\n";
            }
            return 0;
        }
    }while(next_permutation(brute, brute+9));
}
