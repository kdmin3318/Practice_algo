#include<bits/stdc++.h>
using namespace std;

char s[2200][2200];

void star(int x, int y, int z) {
    if(x==1) {
        s[y][z] = '*';
        return;
    }
    for(int i=0;i<3;i++) {
        for(int j=0;j<3;j++) {
            if(i==1&&j==1) continue;
            star(x/3, y + x/3*i, z + x/3*j);
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;

    for(int i=0;i<n;i++)
        fill(s[i], s[i]+n, ' ');

    star(n,0,0);
    for(int i=0;i<n;i++)
        cout<<s[i]<<'\n';
}
