#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x;
    cin >> x;

    if (x % 5 == 0){
        int result = x / 5;
        cout << result << endl;
    }
    else {
        int result = (x / 5) + 1;
        cout << result << endl;
    }

    return 0;
}