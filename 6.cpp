#include <bits/stdc++.h>

using namespace std;

int main() {
    int sum = (100 * 101 / 2) * (100 * 101 / 2);
    for (int i = 1; i <= 100; i++) {
        sum -= i * i;
    }
    printf("%d", sum);
    return 0;
}
