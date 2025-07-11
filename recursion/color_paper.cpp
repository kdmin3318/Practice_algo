#include<bits/stdc++.h>
using namespace std;

int paper[2200][2200];
int cnt[2];

bool check(int x,int y, int z) {
    for(int i=x;i<x+z;i++) {
        for(int j=y;j<y+z;j++) {
            if(paper[x][y]!=paper[i][j]) return false;
        }
    }
    cnt[paper[x][y]]++;
    return true;
}

void cp(int a, int b, int c) {
    if(check(a,b,c)){
        return;
    }
    int new_size = c/2;
    for(int i=0;i<2;i++) {
        for(int j=0;j<2;j++) {
            cp(a+i*new_size,b+j*new_size,new_size);
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    for(int i=0;i<n;i++) 
        for(int j=0;j<n;j++)
            cin>>paper[i][j];
    cp(0,0,n);
    for(int i=0;i<2;i++) 
        cout<<cnt[i]<<"\n";
}
