from math import sqrt

cnt = 0
for n in range(1, 10001):
    numer, denom, period = f'sqrt({n})-{int(sqrt(n))}', 1, 0
    if eval(numer) != 0:
        while True:
            numer, denom = numer.replace('-', '+'), (n - int(numer[numer.find('-'):]) ** 2) // denom
            numer = numer[:numer.find('+')] + str(int(numer[numer.find('+'):]) - denom * (int(eval(numer)) // denom))
            period += 1
            if denom == 1 and numer == f'sqrt({n})-{int(sqrt(n))}':
                break
        cnt += period % 2
print(cnt)
