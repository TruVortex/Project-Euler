ans, totient = (-1, float('inf')), list(range(10000000))
for i in range(2, 10000000):
    if totient[i] == i:
        for j in range(i, 10000000, i):
            totient[j] *= i - 1
            totient[j] //= i
    if sorted(str(totient[i])) == sorted(str(i)) and i / totient[i] < ans[1]:
        ans = (i, i / totient[i])
print(ans[0])
