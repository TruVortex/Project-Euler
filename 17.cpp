#include <bits/stdc++.h>

using namespace std;

int len1[20] = { 4, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8 }, len2[10] = { 0, 0, 6, 6, 5, 5, 5, 7, 6, 6 };

int length(int n) {
    if (1 <= n && n <= 19) {
        return len1[n];
    } else if (20 <= n && n <= 99) {
        return len2[n / 10] + (n % 10 ? len1[n % 10] : 0);
    } else if (100 <= n && n <= 999) {
        return len1[n / 100] + 7 + (n % 100 ? 3 + length(n % 100) : 0);
    }
    return 11;
}

int main() {
    int ans = 0;
    for (int i = 1; i <= 1000; i++) {
        ans += length(i);
    }
    printf("%d", ans);
    return 0;
}
