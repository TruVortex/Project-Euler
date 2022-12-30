#include <bits/stdc++.h>

using namespace std;

int main() {
    long long sum = 0;
    vector<bool> isPrime(2000001, true);
    isPrime[0] = false;
    isPrime[1] = false;
    for (int i = 2; i <= 2000000; i++) {
        if (isPrime[i]) {
            sum += i;
            for (long long j = 1LL * i * i; j <= 2000000; j += i) {
                isPrime[j] = false;
            }
        }
    }
    printf("%lld", sum);
    return 0;
}
