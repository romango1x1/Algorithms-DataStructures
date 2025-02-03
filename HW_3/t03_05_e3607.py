def count_members_in_range(heights, a, b):
    count = 0
    for height in heights:
        if a <= height <= b:
            count += 1
    return count

def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        heights = list(map(int, input().split()))

        a, b = map(int, input().split())

        result = count_members_in_range(heights, a, b)
        print(result)

if __name__ == "__main__":
    main()