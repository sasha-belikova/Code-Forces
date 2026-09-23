#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string n;
    cin >> n;
    string a;
    cin >> a;


    for (char &c : n) {
        c = tolower(c);
    }

    for (char & d : a) {
        d = tolower(d);
    }



    if (a == n) {
        cout << 0 << endl;
    }
    else if (n < a) {
        cout << -1 << endl;
    }
    else {
        cout << 1 << endl;
    }

    
    return 0;
}