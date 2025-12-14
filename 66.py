from math import sqrt


def find_frac(numer, denom, start, sequence):
    if not sequence:
        return numer + start * denom
    return find_frac(denom, numer + sequence.pop() * denom, start, sequence)


ans = (-1, -1)
for d in range(1, 1001):
    numer, denom, sequence = f'sqrt({d})-{int(sqrt(d))}', 1, []
    if eval(numer) != 0:
        while True:
            numer, denom = numer.replace('-', '+'), (d - int(numer[numer.find('-'):]) ** 2) // denom
            sequence.append(int(eval(numer)) // denom)
            numer = numer[:numer.find('+')] + str(int(numer[numer.find('+'):]) - denom * (int(eval(numer)) // denom))
            if denom == 1 and numer == f'sqrt({d})-{int(sqrt(d))}':
                break
        if len(sequence) % 2:
            if (x := find_frac(0, 1, int(sqrt(d)), sequence + sequence[:-1])) > ans[1]:
                ans = (d, x)
        else:
            if (x := find_frac(0, 1, int(sqrt(d)), sequence[:-1])) > ans[1]:
                ans = (d, x)
print(ans[0])
