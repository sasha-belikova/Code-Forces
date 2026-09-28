#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    int n;
    cin >> m >> n;

    int cells = m * n;

    if (cells >= 2){
        if (cells % 2 == 0){
            int result = cells / 2;
            cout << result << endl;
        }
        else {
            int result = (cells - 1) / 2;
            cout << result << endl;
        }
    }
    else {
        cout << 0 << endl;
    }
    
    return 0;
}