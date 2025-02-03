def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def main():
    n = int(input())
    collection = list(map(int, input().split()))

    m = int(input())
    queries = list(map(int, input().split()))

    for query in queries:
        if binary_search(collection, query):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()