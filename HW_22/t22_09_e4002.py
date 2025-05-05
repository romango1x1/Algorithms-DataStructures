import sys
from collections import deque

input = sys.stdin.read().split()


def main():
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)

    color = [ -1 ] * (n + 1)
    is_bipartite = True

    for i in range(1, n + 1):
        if color[i] == -1:
            q = deque()
            q.append(i)
            color[i] = 0
            while q and is_bipartite:
                current = q.popleft()
                for neighbor in adj[current]:
                    if color[neighbor] == -1:
                        color[neighbor] = color[current] ^ 1
                        q.append(neighbor)
                    elif color[neighbor] == color[current]:
                        is_bipartite = False
                        break

    print("YES" if is_bipartite else "NO")


if __name__ == "__main__":
    main()
    