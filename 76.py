from functools import cache


@cache
def count_sums(n, prev):
    if n == 0:
        return 1
    ans = 0
    for i in range(prev, n + 1):
        ans += count_sums(n - i, i)
    return ans


print(count_sums(100, 1) - 1)
