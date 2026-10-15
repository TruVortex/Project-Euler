def area(x1, y1, x2, y2):
    return abs(x1 * y2 - x2 * y1) / 2

cnt = 0
for triangle in open("triangles.txt", "r"):
    x1, y1, x2, y2, x3, y3 = map(int, triangle.split(","))
    cnt += area(x1, y1, x2, y2) + area(x1, y1, x3, y3) + area(x2, y2, x3, y3) == area(x1 - x3, y1 - y3, x2 - x3, y2 - y3)
print(cnt)
