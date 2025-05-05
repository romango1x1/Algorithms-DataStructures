import sys

input = sys.stdin.read().split()


def main():
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    k = int(input[ptr])
    ptr += 1
    a = int(input[ptr])
    ptr += 1
    b = int(input[ptr])
    ptr += 1
    d = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(k):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)

    count = 0

    def dfs(current, path, days):
        nonlocal count
        if current == b and days <= d:
            count += 1
            return
        if days >= d:
            return
        for neighbor in adj[current]:
            if neighbor not in path:
                dfs(neighbor, path + [neighbor], days + 1)

    dfs(a, [a], 0)
    print(count)


if __name__ == "__main__":
    main()
