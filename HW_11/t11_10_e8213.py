def solve(i, left, right, plates, m, res):
    if i == m:
        if left == right:
            res.add(left)
        return
    solve(i + 1, left, right, plates, m, res)
    solve(i + 1, left + plates[i], right, plates, m, res)
    solve(i + 1, left, right + plates[i], plates, m, res)


def main():
    n, m = map(int, input().split())
    barbells = list(map(int, input().split()))
    plates = list(map(int, input().split()))

    res = set()
    solve(0, 0, 0, plates, m, res)

    ans = set()
    for b in barbells:
        for s in res:
            ans.add(b + 2 * s)

    for weight in sorted(ans):
        print(weight)


if __name__ == "__main__":
    main()