#include <bits/stdc++.h>

using namespace std;

int factors[10000];

int main() {
    int ans = 0;
    for (int i = 1; i < 10000; i++) {
        for (int j = 2 * i; j < 10000; j += i) {
            factors[j] += i;
        }
    }
    for (int i = 1; i < 10000; i++) {
        if (factors[i] < 10000 && factors[i] != i && factors[factors[i]] == i) {
            ans += i;
        }
    }
    printf("%d", ans);
    return 0;
}
