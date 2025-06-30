#include<bits/stdc++.h>
using namespace std;

int paper[2200][2200];
int cnt[3]; // cnt[0]: -1개수, cnt[1]: 0개수, cnt[2]: 1개수

bool check(int x, int y, int size) {
    int first = paper[x][y];
    for(int i = x; i < x + size; i++) {
        for(int j = y; j < y + size; j++){
            if(paper[i][j] != first) return false;
        }
    }
    cnt[first + 1]++; // -1이면 cnt[0], 0이면 cnt[1], 1이면 cnt[2]
    return true;
}

void divide(int x, int y, int size) {
    if(check(x, y, size)) {
        return;
    }
    int newSize = size / 3;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            divide(x + i * newSize, y + j * newSize, newSize);
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> paper[i][j];
        }
    }
    
    divide(0, 0, n);
    
    for(int i = 0; i < 3; i++) {
        cout << cnt[i] << "\n";
    }
    
    return 0;
}
