#include <bits/stdc++.h>

using namespace std;

int check[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

int main() {
    int day = 2, ans = 0;
    for (int i = 1901; i <= 2000; i++) {
        check[1] += (i % 4 == 0);
        for (int days : check) {
            day += days;
            if (day % 7 == 0) {
                ans++;
            }
        }
        check[1] -= (i % 4 == 0);
    }
    printf("%d", ans);
    return 0;
}
