import sys

input = sys.stdin.read


def main():
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    edges = data[2:]

    unique_edges = set()
    for i in range(m):
        u = int(edges[2 * i])
        v = int(edges[2 * i + 1])
        if u == v:
            continue
        unique_edges.add((min(u, v), max(u, v)))

    required_edges = n * (n - 1) // 2
    if len(unique_edges) != required_edges:
        print("NO")
        return

    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if (u, v) not in unique_edges:
                print("NO")
                return

    print("YES")


if __name__ == "__main__":
    main()
