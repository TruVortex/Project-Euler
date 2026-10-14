from math import log

pairs, maxx, ans = open('base_exp.txt', 'r').read().splitlines(), 0, -1
for i, pair in enumerate(pairs):
    base, exponent = map(int, pair.split(','))
    num = exponent * log(base)
    if num > maxx:
        maxx = num
        ans = i
print(ans + 1)
