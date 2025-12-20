import itertools

cnt = 0
for cube1 in itertools.combinations(tuple(range(10)), 6):
    if 6 in cube1 or 9 in cube1:
        cube1 += (6, 9)
    for cube2 in itertools.combinations(tuple(range(10)), 6):
        if 6 in cube2 or 9 in cube2:
            cube2 += (6, 9)
        if all((x in cube1 and y in cube2) or (y in cube1 and x in cube2) for x, y in ((0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1))):
            cnt += 1
print(cnt // 2)
