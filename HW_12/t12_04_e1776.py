def is_possible_rearrangement(n, target_sequence):
    stack = []
    current = 1
    for wagon in target_sequence:
        while current <= n and (not stack or stack[-1] != wagon):
            stack.append(current)
            current += 1
        if stack and stack[-1] == wagon:
            stack.pop()
        else:
            return False
    return True


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        while True:
            sequence = list(map(int, input().split()))
            if sequence[0] == 0:
                print()
                break
            if is_possible_rearrangement(n, sequence):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()