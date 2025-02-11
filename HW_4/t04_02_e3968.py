import math


def find_x(C):
    left = 0.0
    right = C

    precision = 1e-10

    while right - left > precision:
        mid = (left + right) / 2
        if mid**2 + math.sqrt(mid) < C:
            left = mid
        else:
            right = mid
    return round((left + right) / 2, 6)


C = float(input())
x = find_x(C)
print("{0:.6f}".format(x))
