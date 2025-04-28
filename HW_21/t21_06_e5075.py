import sys

input = sys.stdin.read


def main():
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    edges = data[2:]

    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    for i in range(m):
        u = int(edges[2 * i])
        v = int(edges[2 * i + 1])
        out_degree[u] += 1
        in_degree[v] += 1

    for vertex in range(1, n + 1):
        print(in_degree[vertex], out_degree[vertex])


if __name__ == "__main__":
    main()
