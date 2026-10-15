def f(coeff, at):
    return sum(c * at ** i for i, c in enumerate(coeff))

def interpolate(points):
    newton_coeff = [point[1] for point in points]
    for i in range(len(newton_coeff) - 2, -1, -1):
        for j in range(i + 1, len(newton_coeff)):
            newton_coeff[j] = (newton_coeff[j] - newton_coeff[j - 1]) / (points[j][0] - points[i][0])
    for i in range(len(newton_coeff) - 2, -1, -1):
        for j in range(i, len(newton_coeff) - 1):
            newton_coeff[j] -= points[i][0] * newton_coeff[j + 1]
    return f(newton_coeff, len(points) + 1)

poly, kernel, ans = (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1), [], 0
for i in range(1, len(poly)):
    kernel.append((i, f(poly, i)))
    ans += interpolate(kernel)
print(ans)
