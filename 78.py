from functools import cache


@cache
def count_sums(n):
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    ans, i = 0, 1
    while ((p1 := i * (3 * i - 1) // 2) <= n) | ((p2 := -i * (3 * -i - 1) // 2) <= n):
        ans += (-1) ** (i - 1) * count_sums(n - p1) + int((-1) ** (-i - 1)) * count_sums(n - p2)
        i += 1
    return ans


n = 1
while count_sums(n) % 1000000:
    n += 1
print(n)
