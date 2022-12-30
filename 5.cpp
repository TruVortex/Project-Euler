#include <bits/stdc++.h>

using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main() {
    long long lcm = 1;
    for (int i = 2; i <= 20; i++) {
        lcm = lcm * i / gcd(lcm, i);
    }
    printf("%lld", lcm);
    return 0;
}
