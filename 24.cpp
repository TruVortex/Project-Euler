#include <bits/stdc++.h>

using namespace std;

int main() {
    int arr[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    for (int i = 0; i < 1000000; i++) {
        next_permutation(arr, arr + 10);
    }
    for (int x : arr) {
        printf("%d", x);
    }
    return 0;
}
