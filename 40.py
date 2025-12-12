from math import prod

d = ''.join(str(n) for n in range(1, 200000))
print(prod(map(int, (d[10 ** i - 1] for i in range(0, 7)))))
