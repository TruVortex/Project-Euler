fact = [1]
for i in range(39):
    fact.append(fact[-1] * (i + 2))
print(fact[-1] // (fact[19] * fact[19]))
