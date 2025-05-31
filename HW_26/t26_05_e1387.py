import sys
import math
import heapq
input = sys.stdin.read().split()


def prim(n, points):
    INF = float('inf')
    total = 0.0
    visited = [False] * n
    min_dist = [INF] * n
    min_dist[0] = 0
    heap = [(0, 0)]

    while heap:
        current_dist, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += math.sqrt(current_dist)
        for v in range(n):
            if not visited[v]:
                dx = points[u][0] - points[v][0]
                dy = points[u][1] - points[v][1]
                dist_sq = dx * dx + dy * dy
                if dist_sq < min_dist[v]:
                    min_dist[v] = dist_sq
                    heapq.heappush(heap, (dist_sq, v))
    return total


def main():
    ptr = 0
    while True:
        n = int(input[ptr])
        ptr += 1
        if n == 0:
            break
        points = []
        for _ in range(n):
            x = int(input[ptr])
            y = int(input[ptr + 1])
            points.append((x, y))
            ptr += 2
        result = prim(n, points)
        print("{0:.2f}".format(result))


main()
