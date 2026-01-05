from math import isqrt


def find_new(n):
    tot = 1 if n % isqrt(n) else isqrt(n)
    for i in range(2, isqrt(n)):
        if n % i == 0:
            tot += i + n // i
    return tot


ans, seen = (-1, -1), set()
for n in range(1, 1000001):
    cur, nseen = find_new(n), [n]
    while cur not in seen and cur not in nseen:
        if cur > 1000000:
            break
        nseen.append(cur)
        cur = find_new(cur)
    if cur in nseen and len(nseen) - nseen.index(cur) > ans[1]:
        ans = (min(nseen[nseen.index(cur):]), len(nseen))
    seen |= set(nseen)
print(ans[0])
