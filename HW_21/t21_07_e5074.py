import sys

input = sys.stdin.read


def main():
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    edges = data[2:]

    degree = [0] * (n + 1)

    for i in range(m):
        u = int(edges[2 * i])
        v = int(edges[2 * i + 1])
        degree[u] += 1
        degree[v] += 1

    for vertex in range(1, n + 1):
        print(degree[vertex])


if __name__ == "__main__":
    main()
