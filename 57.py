cnt, numer, denom = 0, 1, 2
for i in range(1000):
    cnt += len(str(numer + denom)) > len(str(denom))
    numer, denom = denom, 2 * denom + numer
print(cnt)
