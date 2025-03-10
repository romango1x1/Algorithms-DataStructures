max_len = 0


def solve(n, arr):
    global max_len
    max_len = 0
    total_sum = sum(arr)

    if total_sum <= n:
        return total_sum

    if n in arr:
        return n

    for i in range(len(arr)):
        _solve(arr, arr[i], i + 1, n)

    return max_len


def _solve(arr, current_sum, index, n):
    global max_len

    if current_sum > n:
        return

    if current_sum > max_len:
        max_len = current_sum

    if max_len == n:
        return

    for i in range(index, len(arr)):
        _solve(arr, current_sum + arr[i], i + 1, n)


if __name__ == "__main__":
    with open("input.txt") as file:
        for line in file:
            mas = [int(el) for el in line.strip().split()]
            n, s = mas[0], mas[1]
            tracks = mas[2:]
            result = solve(n, tracks)
            print(f"sum:{result}")