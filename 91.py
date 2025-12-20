def orthogonal(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1) == 0


cnt = 0
for x1 in range(51):
    for y1 in range(51):
        if (x1, y1) != (0, 0):
            for x2 in range(x1, 51):
                for y2 in range(51):
                    if ((x2, y2) not in ((0, 0)) + tuple((x1, y) for y in range(y1 + 1)) and
                            (orthogonal(0, 0, x1, y1, x2, y2) or
                             orthogonal(x1, y1, 0, 0, x2, y2) or
                             orthogonal(x2, y2, 0, 0, x1, y1))):
                        cnt += 1
print(cnt)
