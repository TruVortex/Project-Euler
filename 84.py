from bisect import bisect_right
from random import randint

board, tile, double = [0] * 40, 0, 0
for i in range(1000000):
    tile = (tile + (d1 := randint(1, 4)) + (d2 := randint(1, 4))) % 40
    if d1 == d2:
        double += 1
        if double == 3:
            double = 0
            tile = 10
    else:
        double = 0
    if tile == 30:
        tile = 10
    elif tile in (2, 17, 33):
        match randint(1, 16):
            case 1:
                tile = 0
            case 2:
                tile = 10
    elif tile in (7, 22, 36):
        tile = (0, 10, 11, 24, 39, 5, (r := (5, 15, 25, 35, 45)[bisect_right((5, 15, 25, 35, 45), tile)] % 40), r, (12, 28, 52)[bisect_right((12, 28, 52), tile)] % 40, tile - 3, *([tile] * 6))[randint(0, 15)]
    board[tile] += 1
print(''.join(f'{idx:0>2}' for cnt, idx in sorted(zip(board, range(40)), reverse=True)[:3]))
