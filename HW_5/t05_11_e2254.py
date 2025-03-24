def max_rice_trucks(R, L, B, X):
    left = 0
    max_trucks = 0
    total_cost = 0

    for right in range(R):
        total_cost += X[right] - X[(left + right) // 2]

        while total_cost > B:
            total_cost -= X[(left + right + 1) // 2] - X[left]
            left += 1

        max_trucks = max(max_trucks, right - left + 1)

    return max_trucks


R, L, B = map(int, input().split())
X = [int(input()) for _ in range(R)]

print(max_rice_trucks(R, L, B, X))