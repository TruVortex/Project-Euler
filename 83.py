from heapq import heappop, heappush

matrix, dir = [list(map(int, line.split(','))) for line in open('input', 'r')], ((-1, 0), (1, 0), (0, -1), (0, 1))
dist, pq = [[float('inf')] * 80 for i in range(80)], [(matrix[0][0], 0, 0)]
dist[0][0] = matrix[0][0]
while pq[0][1:] != (79, 79):
    cur = heappop(pq)
    for dr, dc in dir:
        if 0 <= (nr := cur[1] + dr) < 80 and 0 <= (nc := cur[2] + dc) < 80 and (nd := cur[0] + matrix[nr][nc]) < dist[nr][nc]:
            dist[nr][nc] = nd
            heappush(pq, (nd, nr, nc))
print(pq[0][0])
