import sys
sys.setrecursionlimit(1500)


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)

    def print_preorder(self):
        stack = []
        current = self
        while True:
            if current is not None:
                print(current.key, end="")
                if current.right is not None:
                    stack.append(current.right)
                current = current.left
            elif stack:
                current = stack.pop()
            else:
                break


def main():
    with open("input.txt") as file:
        nodes = [line.strip() for line in file if line.strip() != "*"]

    all_chars = []
    for line in reversed(nodes):
        all_chars.extend(line)

    if not all_chars:
        return

    root = BinaryTree(all_chars[0])
    for ch in all_chars[1:]:
        root.insert(ch)

    root.print_preorder()


if __name__ == "__main__":
    main()
