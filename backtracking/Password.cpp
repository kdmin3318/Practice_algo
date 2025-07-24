#include<bits/stdc++.h>
using namespace std;

int l,c;
char arr[20];
char result[20];
int con = 0;
int vo = 0;

void solve(int k, int st){
    if(k==l){
        if(con>=2 && vo>=1){
            for(int i=0;i<l;i++) cout<<result[i];
            cout<<"\n";
            return;
        }
    }

    for(int i=st;i<c;i++) {
        result[k] = arr[i];
        if(arr[i]=='a' || arr[i]=='e' || arr[i]=='i' || arr[i]=='o' || arr[i]=='u') vo++;
        else con++;
        solve(k+1,i+1);
        if(arr[i]=='a' || arr[i]=='e' || arr[i]=='i' || arr[i]=='o' || arr[i]=='u') vo--;
        else con--;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>l>>c;
    for(int i=0;i<c;i++) cin>>arr[i];
    sort(arr, arr+c);
    solve(0,0);
}
