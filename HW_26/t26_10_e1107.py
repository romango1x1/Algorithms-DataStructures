import sys
input = sys.stdin.read


def find(parent, u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u


def union(parent, rank, u, v):
    u_root = find(parent, u)
    v_root = find(parent, v)
    if u_root == v_root:
        return False
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    else:
        parent[v_root] = u_root
        if rank[u_root] == rank[v_root]:
            rank[u_root] += 1
    return True


def kruskal(n, edges, exclude_edge=None):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total_cost = 0
    edges_used = []
    edges_sorted = sorted(edges, key=lambda x: x[2])

    for edge in edges_sorted:
        if exclude_edge and edge == exclude_edge:
            continue
        u, v, w = edge
        if union(parent, rank, u, v):
            total_cost += w
            edges_used.append(edge)
            if len(edges_used) == n - 1:
                break
    if len(edges_used) != n - 1:
        return float('inf'), None
    return total_cost, edges_used


def main():
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))

    first_mst_cost, first_mst_edges = kruskal(n, edges)

    second_mst_cost = float('inf')

    for excluded_edge in first_mst_edges:
        current_cost, _ = kruskal(n, edges, excluded_edge)
        if current_cost < second_mst_cost:
            second_mst_cost = current_cost

    print(first_mst_cost, second_mst_cost)


if __name__ == "__main__":
    main()
