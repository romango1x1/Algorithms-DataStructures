import sys

input = sys.stdin.read


def main():
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    edges = data[2:]

    seen = set()
    has_multi_edges = False

    for i in range(m):
        u = int(edges[2 * i])
        v = int(edges[2 * i + 1])
        edge = (u, v)
        if edge in seen:
            has_multi_edges = True
            break
        seen.add(edge)

    print("YES" if has_multi_edges else "NO")


if __name__ == "__main__":
    main()
