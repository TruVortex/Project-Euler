#include <bits/stdc++.h>

using namespace std;

int main() {
    int maxx = 0, idx = 0;
    for (int i = 2; i < 1000; i++) {
        map<int, int> lookup;
        for (int j = 0, cur = 1;; j++) {
            if (lookup.count(cur)) {
                if (j - lookup[cur] > maxx) {
                    maxx = j - lookup[cur];
                    idx = i;
                }
                break;
            } else {
                lookup[cur] = j;
                cur *= 10;
                cur %= i;
            }
        }
    }
    printf("%d", idx);
    return 0;
}
