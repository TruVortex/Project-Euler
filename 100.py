b, t = 15, 21
while t <= 10 ** 12:
    b, t = 3 * b + 2 * t - 2, 4 * b + 3 * t - 3
print(b)
