#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    string s_numbers;
    string result;

    for (char symb : s) {
        if (symb != '+') {
            s_numbers += symb;
        }
    }

    sort(s_numbers.begin(), s_numbers.end());

    for (int i = 0; i < s_numbers.size(); i++) {
        if (i > 0) {
            result += '+';
        }
        result += s_numbers[i];
    }

    cout << result << endl;

    return 0;
}