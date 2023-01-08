#include <bits/stdc++.h>

using namespace std;

bool possible[28124];
int nums[28124];

int main() {
    for (int i = 1; i <= 28123; i++) {
        for (int j = 2 * i; j <= 28123; j += i) {
            nums[j] += i;
        }
    }
    vector<int> abundant;
    for (int i = 1; i <= 28123; i++) {
        if (nums[i] > i) {
            abundant.push_back(i);
        }
    }
    for (int num1 : abundant) {
        for (int num2 : abundant) {
            if (num1 + num2 <= 28123) {
                possible[num1 + num2] = true;
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= 28123; i++) {
        if (!possible[i]) {
            ans += i;
        }
    }
    printf("%d", ans);
    return 0;
}
