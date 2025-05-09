import sys
from collections import deque

input = sys.stdin.read().split()


def main():
    ptr = 0
    n = int(input[ptr])
    m = int(input[ptr + 1])
    ptr += 2
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        i = int(input[ptr])
        j = int(input[ptr + 1])
        ptr += 2
        adj[i].append(j)
        adj[j].append(i)

    visited = [False] * (n + 1)
    components = []

    for node in range(1, n + 1):
        if not visited[node]:
            queue = deque()
            queue.append(node)
            visited[node] = True
            component = []

            while queue:
                current = queue.popleft()
                component.append(current)
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            components.append(component)

    print(len(components))

    for component in components:
        print(len(component))
        print(" ".join(map(str, sorted(component))) + " ")


if __name__ == "__main__":
    main()
