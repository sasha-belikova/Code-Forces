#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector <string> a(n);    
    for (int k = 0; k < n; k++){
        cin >> a[k];
    }

    int x = 0;

    for (string operation : a){
        if (operation == "++X" || operation == "X++") {
            x++;
        }
        else {
            x--;
        }
    }

    cout << x << endl;
    
    return 0;
}