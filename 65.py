def find_frac(d, numer, denom):
    if d == 1:
        return numer + 2 * denom
    if d % 3 == 0:
        return find_frac(d - 1, denom, numer + 2 * (d // 3) * denom)
    return find_frac(d - 1, denom, numer + denom)


print(sum(int(digit) for digit in str(find_frac(100, 0, 1))))
