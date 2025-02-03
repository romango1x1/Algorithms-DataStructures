def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def count_occurrences(arr, target):
    lower = lower_bound(arr, target)
    upper = upper_bound(arr, target)
    return upper - lower


def main():
    n = int(input())
    colors = list(map(int, input().split()))

    m = int(input())
    queries = list(map(int, input().split()))

    for query in queries:
        count = count_occurrences(colors, query)
        print(count)


if __name__ == "__main__":
    main()