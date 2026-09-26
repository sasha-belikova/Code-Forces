#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a;
    int b;
    cin >> a >> b;

    int result = 0;

    while (a <= b){
        a = a *3;
        b = b * 2;
        result += 1;
    }

    cout << result << endl;
    
    return 0;
}