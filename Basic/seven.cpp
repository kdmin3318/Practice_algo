#include<bits/stdc++.h>
using namespace std;
int search(int a[], int sum) {
    for(int i=0;i<8;i++) {
        for(int j=i+1;j<9;j++){
            if(a[i] + a[j] == sum-100) {
                a[i] = 0;
                a[j] = 0;
                return 0;
            }
        }
    }
    return 1;
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int arr[9], sum=0;
    for(int i=0;i<9;i++) {
        cin>>arr[i];
        sum += arr[i];
    }
    if(search(arr,sum)==0) {
        sort(arr,arr+9);
        for(int i=2;i<9;i++) {
            cout << arr[i] << "\n";
        }
    }
}
