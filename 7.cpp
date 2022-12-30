#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<bool> isPrime(1000001, true);
    isPrime[0] = false;
    isPrime[1] = false;
    int cnt = 0;
    for (int i = 2; i <= 1000000; i++) {
        if (isPrime[i]) {
            cnt++;
            if (cnt == 10001) {
                printf("%d", i);
                return 0;
            }
            for (long long j = 1LL * i * i; j <= 1000000; j += i) {
                isPrime[j] = false;
            }
        }
    }
    return 0;
}
