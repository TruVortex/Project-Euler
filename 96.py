def solve(grid, x, y):
    if x == 0 and y == 9:
        return grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
    nx, ny = (x + 1) % 9, y + (x == 8)
    if grid[x][y]:
        return solve(grid, nx, ny)
    pos_num = set(range(1, 10)) - (get_square(grid, x, y) | set(grid[x]) | {grid[r][y] for r in range(9)})
    if not pos_num:
        return 0
    for pos in pos_num:
        grid[x][y] = pos
        if top_left := solve(grid, nx, ny):
            return top_left
        grid[x][y] = 0
    return 0

def get_square(grid, x, y):
    square = set()
    for i in range(3):
        for j in range(3):
            square |= {grid[x - x % 3 + i][y - y % 3 + j]}
    return square

lines, total = open("sudoku.txt", "r").read().splitlines(), 0
for i in range(1, len(lines), 10):
    total += solve([list(map(int, line)) for line in lines[i:i+9]], 0, 0)
print(total)
