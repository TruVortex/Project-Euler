ans, totient = 0, list(range(1000001))
for i in range(2, 1000001):
    if totient[i] == i:
        for j in range(i, 1000001, i):
            totient[j] *= i - 1
            totient[j] //= i
    ans += totient[i]
print(ans)
