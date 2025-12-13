import itertools


def find_pos(prev, order):
    global polygonals
    if not order:
        return [(prev, 0)]
    return [(pos, total + p) for p in polygonals[order[0]] if str(p)[:2] == str(prev)[2:] for pos, total in find_pos(p, order[1:])]


polygonals = [[p for n in range(1, 141) if 1000 <= (p := n * (n + 1) // 2) <= 9999],
              [p for n in range(1, 141) if 1000 <= (p := n * n) <= 9999],
              [p for n in range(1, 141) if 1000 <= (p := n * (3 * n - 1) // 2) <= 9999],
              [p for n in range(1, 141) if 1000 <= (p := n * (2 * n - 1)) <= 9999],
              [p for n in range(1, 141) if 1000 <= (p := n * (5 * n - 3) // 2) <= 9999],
              [p for n in range(1, 141) if 1000 <= (p := n * (3 * n - 2)) <= 9999]]
for p in polygonals[0]:
    for order in itertools.permutations(range(1, 6)):
        for pos, total in find_pos(p, order):
            if str(p)[:2] == str(pos)[2:]:
                print(total + p)
