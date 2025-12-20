from functools import cache


@cache
def endpoint(n):
    if n in (1, 89):
        return n
    return endpoint(sum(int(d) ** 2 for d in str(n)))


print(sum(endpoint(n) == 89 for n in range(1, 10000000)))
