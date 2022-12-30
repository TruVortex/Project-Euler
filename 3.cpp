#include <bits/stdc++.h>

using namespace std;

int main() {
    int ans = 0;
    long long n = 600851475143;
    for (int i = 2; i <= sqrt(n); i++) {
        while (n % i == 0) {
            n /= i;
            ans = max(ans, i);
        }
    }
    printf("%d", max(ans, (int) n));
    return 0;
}
