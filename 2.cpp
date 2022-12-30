#include <bits/stdc++.h>

using namespace std;

int main() {
    int sum = 0, a = 1, b = 1;
    while (b <= 4000000) {
        if (b % 2 == 0) {
            sum += b;
        }
        b += a;
        a = b - a;
    }
    printf("%d", sum);
    return 0;
}
