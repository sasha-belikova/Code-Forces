#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string w = "CHAT WITH HER!";
    string m = "IGNORE HIM!";

    string n;
    cin >> n;

    vector <char> list;

    for (char &letter : n ){
        if (find(list.begin(), list.end(), letter) == list.end()) {
            list.push_back(letter);
        }
    }

    if (list.size() % 2 == 0){
        cout << w << endl;
    }
    else {
        cout << m << endl;
    }
    
    return 0;
}