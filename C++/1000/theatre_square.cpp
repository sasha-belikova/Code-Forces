#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m, a;
    cin >> n >> m >> a;

    long long  part_n = (n + a - 1) / a;
    long long  part_m = (m + a - 1) / a;

    long long  result = part_n * part_m;

    std::cout << result << std::endl;


    return 0;
}