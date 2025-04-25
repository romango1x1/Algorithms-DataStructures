import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index, value):
        pos = self.size + index
        self.tree[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree[pos] = self.tree[pos << 1] + self.tree[pos << 1 | 1]

    def prefix_sum(self, l, r):
        res = 0
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res

    def max_people(self, capacity):
        if self.tree[1] <= capacity:
            return self.n
        l, r = 0, self.n
        while l < r:
            m = (l + r) // 2
            if self.prefix_sum(0, m + 1) <= capacity:
                l = m + 1
            else:
                r = m
        return l

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    tree = SegmentTree(weights)
    m = int(input())

    for _ in range(m):
        parts = input().split()
        t = int(parts[0])
        if t == 1:
            v = int(parts[1])
            print(tree.max_people(v))
        elif t == 2:
            x = int(parts[1]) - 1
            y = int(parts[2])
            tree.update(x, y)


if __name__ == "__main__":
    main()
