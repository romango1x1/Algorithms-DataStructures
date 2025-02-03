def decimal_to_binary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n //= 2
    binary.reverse()
    return binary

def binary_to_decimal(binary):
    decimal = 0
    length = len(binary)
    for i in range(length):
        decimal += binary[i] * (1 << (length - 1 - i))
    return decimal

def generate_cyclic_shifts(binary):
    shifts = []
    current = binary.copy()
    for _ in range(len(binary)):
        current = current[1:] + [current[0]]  # Лівий циклічний зсув
        shifts.append(current.copy())
    return shifts

def main():
    n = int(input())

    binary = decimal_to_binary(n)

    shifts = generate_cyclic_shifts(binary)

    max_decimal = 0
    for shift in shifts:
        decimal = binary_to_decimal(shift)
        if decimal > max_decimal:
            max_decimal = decimal

    print(max_decimal)

if __name__ == "__main__":
    main()