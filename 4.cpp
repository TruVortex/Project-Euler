#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans = 0;
    for (int i = 100; i < 1000; i++) {
        for (int j = 100; j < 1000; j++) {
            string str = to_string(i * j);
            if (str == string(str.rbegin(), str.rend())) {
                ans = max(ans, i * j);
            }
        }
    }
    printf("%d", ans);
    return 0;
}
