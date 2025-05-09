import sys

sys.setrecursionlimit(1 << 25)


def main():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        rev_adj[v].append(u)

    visited = [False] * (n + 1)
    order = []

    def dfs(node):
        stack = [(node, False)]
        while stack:
            current, processed = stack.pop()

            if processed:
                order.append(current)
                continue
            if visited[current]:
                continue
            visited[current] = True
            stack.append((current, True))

            for neighbor in adj[current]:
                if not visited[neighbor]:
                    stack.append((neighbor, False))

    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node)

    visited = [False] * (n + 1)
    component = [0] * (n + 1)
    current_component = 1

    def reverse_dfs(node):
        stack = [node]
        visited[node] = True
        component[node] = current_component
        while stack:
            current = stack.pop()
            for neighbor in rev_adj[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    component[neighbor] = current_component
                    stack.append(neighbor)

    for node in reversed(order):
        if not visited[node]:
            reverse_dfs(node)
            current_component += 1

    print(current_component - 1)
    print(" ".join(map(str, component[1:])))


if __name__ == "__main__":
    main()
