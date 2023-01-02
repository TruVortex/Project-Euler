#include <bits/stdc++.h>

using namespace std;

int factorize(int n) {
    int ans = 0;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            ans++;
            if (n / i != i) {
                ans++;
            }
        }
    }
    return ans;
}

int main() {
    int i = 0;
    while (1) {
        if (factorize(i * (i + 1) / 2) > 500) {
            printf("%d", i * (i + 1) / 2);
            break;
        }
        i++;
    }
    return 0;
}
