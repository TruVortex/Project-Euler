#include <bits/stdc++.h>

using namespace std;

int main() {
    for (int i = 1; i <= 998; i++) {
        for (int j = i + 1; j <= 999 - i; j++) {
            if (i * i + j * j == (1000 - i - j) * (1000 - i - j)) {
                printf("%d", i * j * (1000 - i - j));
            }
        }
    }
    return 0;
}
