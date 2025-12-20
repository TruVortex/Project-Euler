def find_prod_sum(prod, total, cnt, prev):
    global prod_sums
    if (k := prod - total + cnt) <= 12000:
        prod_sums[k] = min(prod_sums[k], prod)
        for i in range(prev, (12000 // prod) * 2 + 1):
            find_prod_sum(prod * i, total + i, cnt + 1, i)


prod_sums = [float('inf')] * 12001
find_prod_sum(1, 1, 1, 2)
print(sum(set(prod_sums[2:])))
