//틀린 이유를 모르겠음
// #include<bits/stdc++.h>
// using namespace std;

// int n;
// stack<int> s;

// int main(void) {
//     ios::sync_with_stdio(0);
//     cin.tie(0);

//     cin>>n;
//     int h, ans=0;
//     while(n--) {
//         cin>>h;
//         ans+=s.size();
//         while(!s.empty()&&s.top()<h) s.pop();
//         s.push(h);
//     }
//     cout<<ans;
// }

#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  stack<pair<int, int>> S;
  long long ans = 0;
  while (n--) {
    int h;
    cin >> h;
    int cnt = 1;
    while (!S.empty() && S.top().X <= h) {
      ans += S.top().Y;
      if (S.top().X == h) cnt += S.top().Y;
      S.pop();
    }
    if (!S.empty()) ans++;
    S.push({h, cnt});
  }
  cout << ans;
}
