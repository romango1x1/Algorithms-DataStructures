def f(x):
    return x**3 + 4*x**2 + x - 6


def find_root():
    left = 0.0
    right = 2.0

    precision = 1e-10

    while right - left > precision:
        mid = (left + right) / 2
        if f(mid) < 0:
            left = mid
        else:
            right = mid

    return round((left + right) / 2, 10)


root = find_root()
print("{0:.10f}".format(root))
