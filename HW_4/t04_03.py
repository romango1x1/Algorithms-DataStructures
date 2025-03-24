def f(x):
    return x**3 + x + 1


def find_min_x():
    left = 0.0
    right = 10.0
    precision = 1e-10

    while right - left > precision:
        mid = (left + right) / 2
        if f(mid) <= 5:
            left = mid
        else:
            right = mid

    return round(right, 10)


min_x = find_min_x()
print("{0:.10f}".format(min_x))
